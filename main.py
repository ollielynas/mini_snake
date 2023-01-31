t=20
s=[0]
a='|'
f=0
r=range
c=1
p=print
g={'a':-1,'w':-t,'d':1,'s':t,1:'#',0:' ',2:'F'}
from msvcrt import *
import time,random as k
while True:
	time.sleep(0.3)
	if kbhit():c=g[getwch()]
	s+=[s[-1]+c]
	if s[-1]in s[:-1]or s[-1]not in r(t*t)or c in r(-1,2)and s[-1]//t!=s[-2]//t:quit()
	if f in s:f=k.choice(r(t*t))
	else:del s[0]
	p('\x1b[2J');p('-'*t)
	for i in r(t):p(a+''.join([g[int(i*t+j in s)+2*int(i*t+j==f)]for j in r(t)])+a)
	p('-'*t)