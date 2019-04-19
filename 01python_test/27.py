# -*- coding:utf-8 -*-

def trim(s):
	if s[0:1] == ' ' and s[-1:] == ' ':
		return s[1:-1]
	elif s[0:1] == ' ':
		return s[1:]
	elif s[-1:] == ' ':
		return s[0:-1]
	else:
		return s[0:]
print(trim(' abc '))