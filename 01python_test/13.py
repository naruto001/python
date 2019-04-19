a = input('height:')
height = float(a)
b = input('weight:')
weight = float(b)
dou = height * height
BMI = weight/dou

if BMI <18.5:
	print(BMI)
	print('thin')
elif BMI<25:
	print(BMI)
	print('normal')
elif BMI<32:
	print(BMI)
	print('fat')
else:
	print(BMI)
	print('fater')