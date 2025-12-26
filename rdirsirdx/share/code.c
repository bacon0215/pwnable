#include <stdio.h>
#include <stdlib.h>

void setup() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

char input[0x20];

int main(void) {
    setup();

    int select = 0;
    unsigned long long rdi = 0;
    unsigned long long rsi = 0;
    unsigned long long rdx = 0; 

    while(1) {
        printf("RDI: ");    scanf("%llu", &rdi);
        printf("RSI: ");    scanf("%llu", &rsi);
        printf("RDX: ");    scanf("%llu", &rdx);
        
        printf("\n(1) read(rdi, rsi, rdx)\n");
        printf("(2) write(rdi, rsi, rdx)\n");
        printf("(3) systme(rdi)\n");
        printf("(4) exit(rdi)\n");
        printf("Your choice: ");
        scanf("%d", &select);
        switch(select) {
            case 1:
                printf("read(%d, 0x%llx, %x)\n", rdi, rsi ,rdx);
                read(rdi, rsi, rdx);
                break;
            case 2:
                printf("write(%d, 0x%llx, %x)\n", rdi, rsi ,rdx);
                write(rdi, rsi, rdx);
                break;
            case 3:
                printf("system(0x%llx)", rdi);
                system(rdi);
                break;
            case 4:
                exit(rdi);
                break;
            default:
                break;
        }
    }

    return 0;
}