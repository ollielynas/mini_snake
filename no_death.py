from msvcrt import *
import time,random as k
t=20;s=[0];f=0;r=range;c=1;g={'a':-1,'w':-t,'d':1,'s':t,1:'#',0:' ',2:'F', 3:'F'}
while 1:
	time.sleep(1)
	if kbhit():c=g[getwch()]
	s+=[s[-1]+c]
	if f in s:f=k.choice(r(t*t))
	else:del s[0]
	for i in r(t):print(''.join([g[int(i*t+j in s)+2*int(i*t+j==f)]for j in r(t)]))
