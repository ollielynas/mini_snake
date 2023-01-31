import math
import zlib
import sys
u = []
for i in range(10000):
    if chr(i).isprintable() and chr(i):
      u += [chr(i)]



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

print("preconcession")
o = b'RIFFr"\'kWAVEfmt \x10kkk\x01k\x01kD\xackkD\xackk\x01k\x08kdataN"\'k'.replace(
    b'k', b'\x00')



o = b'RIFFr"\'kWAVEfmt \x10kkk\x01k\x01kD\xackkD\xackk\x01k\x08kdataN"\'k'.replace(
    b'k', b'\x00')
a=[]
c2 = zlib.compress(bytes((int(127*math.sin(2**(0//7/12)*A/14.2)*(0>6)+128)for A in range([1,2,3,4,6,8,10][0%7]*5802))))
c_int = int.from_bytes(c2, byteorder=sys.byteorder)

print("-----------------")
a = v2r(c_int)
print(a)
print(190-len(a))
# final_string = zlib.decompress(r2v(a).to_bytes(250, 'little'))

for k in zlib.decompress(r2v(a).to_bytes(250, 'little')):
    k -= 34
    o += bytes(int(127*math.sin(2**(k//7/12)*i/14.2)*(k > 6)+128)
               for i in range([1, 2, 3, 4, 6, 8, 10][k % 7]*5802))
open('s.wav', 'wb').write(o)

# exec(zlib.decompress(c2))
