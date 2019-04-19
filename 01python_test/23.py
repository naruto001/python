# -*- coding:utf-8 -*-
import math
A = input('请输入a:')
a = int(A)
B = input('请输入b:')
b = int(B)
C = input('请输入c:')
c = int(C)


def fcs(a,b,c):
	x = b*b-4*a*c 
	y = 2*a
	x1 = (math.sqrt(x)-b)/y
	x2 = (-math.sqrt(x)-b)/y
	return x1,x2

print(fcs(a,b,c))
