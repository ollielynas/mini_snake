from msvcrt import *
import time,random as k
t=20;s=[0];a='|';f=0;r=range;c=1;p=print;g={'a':-1,'w':-t,'d':1,'s':t}
while True:
	time.sleep(0.3);p('\x1b[2J')
	if kbhit():c=g[getwch()]
	s+=[s[-1]+c]
	if f in s:f=k.choice(r(t*t))
	else:del s[0]
	for i in r(t):p([int(i*t+j in s)+int(i*t+j==f) for j in r(t)])
