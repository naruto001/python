# -*- coding:utf-8 -*-
def findMaxAndMin(L):
  if( not isinstance(L,( list )) or L == [] ): return (None, None)
  max = L[0]
  min = L[0]
  for i,x in enumerate(L) :
    if( x <= min ):
      min = x
    elif x > max:
      max = x
  return ( max , min )

print( findMaxAndMin( [1,4,7,2,3,4,66,5,11,9,22,55] ) )
print( findMaxAndMin( 1 ) )
print( findMaxAndMin( [] ) )