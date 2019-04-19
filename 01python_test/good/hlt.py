# -*- coding:utf-8 -*-
def hanoi(n,a,buffer,c):
	if n == 1:
		print(a,'--->',c)
	else:
		hanoi(n-1,a,c,buffer)
		hanoi(1,a,buffer,c)
		hanoi(n-1,buffer,a,c)
hanoi(3,'A','B','C')		