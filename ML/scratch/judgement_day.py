def XOR_10(a, b):
   if a==0 and b==0:
      return 0
   if a==0 and b==1:
      return 1
   if a==1 and b==0:
      return 1
   if a==1 and b==1:
      return 0

d = bin(1819520040).lstrip('0b')
print d

arr = [bin(ord(x)).lstrip('0b') for x in 'system.ai']

s = ''
for x in arr:
   s += x

s_ORG = s[:len(d)]

print s
print ' ' * (len(s) - len(d)) + d

s_XOR = ''
shift = len(s) - len(d)
for i in range(len(d)):
   s_XOR += str(XOR_10(int(s[i + shift]), int(d[i])))

s_TOTAL = s_ORG + s_XOR
print s_TOTAL

