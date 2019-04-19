#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
def quadratic(a,b,c):
    q=b*b-4*a*c
    if q>0:
        x1=(-b+math.sqrt(q))/a/2
        x2=(-b-math.sqrt(q))/a/2
        return x1,x2
    elif q==0:
        x1=-b/a/2
        x2=x1
        return x1,x2
    else:
        pass
        return ()

print('input a,b,c :')
a=float(input('a:'))
b=float(input('b:'))
c=float(input('c:'))
q=quadratic(a,b,c)
q=set(list(q))
# print('q =',q)
if len(q)==2:
    for x in q:
        print(x)
elif len(q)==1:
    for x in q:
        print(x)
else:
    print('None')