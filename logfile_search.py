log1=open('/Users/kmallick/Documents/python_aura/log1.txt','r')
log1_read=log1.read()

cnt=log1_read.count('warning')

log1.close()


log2=open('/Users/kmallick/Documents/python_aura/log2.txt','r')
log2_read=log2.read()

cnt=log2_read.count('warning')

log2.close()