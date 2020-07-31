#I am a comment (Testing for upload)
x = 5
#當佢地係問題咁問人
print(x != 5) # checking if both sides are not the same (False)
print(x > 2)
print(x < 2)
print(x >= 2)
print(x <= 2)
y = 2
print(y)
z = (x + y)
print(z)
price = 10
pen = 0.38
name = 'Oliver'
print(price, pen, name)

name = input('who are you?')
print('HI', name)

height = input('what is your height?')
print(height)

weight = input('what is your weight')
print(weight)

#記得最尾要加':'
rain = input('今日有無落雨')
if rain == '有':
	print('帶遮')
	print('買野食')
	print('睇戲')
	if rain == '無':
		print('拜拜')

age = input('你幾大?')#因為age係字, 3係實數字;不同,計不了,所以要做casting(轉型)
age = int(age)#casting
if age >= 3:
	print('咁大')
if age <= 3:
	print('咁細')

celsius = input('input celsius')
celsius = int(celsius)#or float(for小數)
fahrenheit = celsius * 9 / 5 + 32
print (fahrenheit, 'F')