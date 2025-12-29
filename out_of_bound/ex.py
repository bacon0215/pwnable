from pwn import *

binary = "./banking"
p = process(binary)
e = ELF(binary)
l = e.libc