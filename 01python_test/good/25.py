# -*- coding:utf-8 -*-
import math
def fcs(a,b,c):
	aaa = pow(b,2)-4*a*c
	if a!= 0 and aaa>0:
		x1 = (-b+math.sqrt(aaa))/(2*a)
		x2 = (-b-math.sqrt(aaa))/(2*a)
		return x1,x2
	elif a!=0 and aaa ==0:
		return -b/(2*a)
	elif a!=0 and aaa<0:
		x1 = str(-b/(2*a)) +'+'+str(math.sqrt(-aaa)/(2*a))+'i'
		x2 = str(-b/(2*a)) +'-'+str(math.sqrt(-aaa)/(2*a))+'i'
		return x1,x2
	elif a==0 and b!=0:
		return -c/b
	else:
		return '没有解'

if __name__ == '__main__':
	a =input('请输入a:')
	b =input('请输入b:')
	c =input('请输入c:')
	print( fcs( float(a), float(b), float(c) ) )
	