from msvcrt import *
import time,random as k
t=20;s=[0];f=0;r=range;c=1;p=print;g={'a':-1,'w':-t,'d':1,'s':t,1:'#',0:' ',2:'F'}
while True:
	time.sleep(0.3)
	if kbhit():c=g[getwch()]
	s+=[s[-1]+c]
	if f in s:f=k.choice(r(t*t))
	else:del s[0]
	p('\x1b[2J')
	for i in r(t):p(''.join([g[int(i*t+j in s)+2*int(i*t+j==f)]for j in r(t)]))
