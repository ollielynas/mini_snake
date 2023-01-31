import zlib, sys
u = []
for i in range(1000000):
    if chr(i).isprintable() and chr(i):
      u+=[chr(i)]

def v2r(num):
  result = ''
  while num > 0:
    result = u[num % len(u)] + result
    num = num // len(u)
  return result

def r2v(data):
  num = 0
  for char in data:
    num = len(u) * num + u[:len(u)].index(char)
  return num






v2 = open("no_death.py").read()

c2 = zlib.compress(v2.encode())
c_int = int.from_bytes(c2, byteorder=sys.byteorder)

print("-----------------")
a = v2r(c_int)
print(a)
print(190-len(a))
# final_string = zlib.decompress(r2v(a).to_bytes(250, 'little'))
#exec(zlib.decompress(r2v(a).to_bytes(254, 'little')))







#exec(zlib.decompress(c2))
