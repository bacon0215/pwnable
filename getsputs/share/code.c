/* gcc -o getsputs code.c -fno-stack-protector -no-pie */
#include <stdio.h>
#include <stdlib.h>

__asm("pop %rdi");
__asm("ret");

void setup() {
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

int main(void) {
    char buf[0x50];
    setup();

    gets(buf);
    puts(buf);

    return 0;
}