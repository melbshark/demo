from pwn import *

lines = [
'from pwn import *',
r'r = remote("google.com",80)',
r'r.sendline("GET /\r\n\r\n")',
r'print repr(r.recvline())',
'print shellcraft.sh()',
'print enhex(asm(shellcraft.sh()))',
'context.arch="arm"',
'sc = alphanumeric(asm(shellcraft.sh()))',
'print hexdump(sc)',
'io = run_shellcode(sc)',
'io.sendline("id")',
'io.sendline("exit")',
'print io.recvall()'
]

for line in lines:
    print '>>> %s' % line
    exec(line)

print '''
# Next, you might want to try some debugging?
#
# >>> p = process('/bin/bash')
# >>> gdb.attach(p, \'\'\'
# ... break echo_builtin
# ... continue
# ... \'\'\')
# >>> p.sendline('echo hello, world')
# >>> p.recvline()
'''
