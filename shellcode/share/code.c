#include <stdio.h>
#include <stdlib.h>

void setup() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

unsigned char shellcode[] = "\\x48\\x31\\xf6\\x56\\x48\\xbf\\x2f\\x62\\x69\\x6e\\x2f\\x2f\\x73\\x68\\x57\\x54\\x5f\\x6a\\x3b\\x58\\x99\\x0f\\x05";

int main(void) {
    unsigned long long canary = 0xdeadbeefcafebabe;
    char buf[0x50];
    setup();

    printf("[Stage 1] Get Useful Information\n");
    printf("Address of RBP - 0x60 (Buffer): %p\n", buf);
    printf("Address of RBP - 0x08 (Canary): %p\n", &canary);
    printf("Address of RBP + 0x00 (SFP): %p\n", buf + 0x60);
    printf("Address of RBP + 0x08 (RET): %p\n", buf + 0x68);
    printf("Value of canary: 0x%llx (It doesn't change!)\n", canary); 
    printf("Shellcode: \"%s\"\n", shellcode);

    printf("\n[Stage 2] Overwrite Return Addrss to Stack Address\n");
    printf("Input : ");
    read(0, buf, 0x100);

    printf("\n[Stage 3] Check Canary (You should consider the fixed-canary!)\n");
    if(canary != 0xdeadbeefcafebabe) {
        printf("Stack Smashing Detected! (Canary : 0x%llx)\n", canary);
        exit(1);
    }
    printf("value of RBP + 0x00 (SFP) : 0x%llx\n", *(unsigned long long *)(buf + 0x60));
    printf("value of RBP + 0x08 (RET) : 0x%llx\n\n", *(unsigned long long *)(buf + 0x68));

    return 0;
}