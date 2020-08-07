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
name = 'ABC'
print(price, pen, name)

name = input('who are you?')
print('HI', name)

#記得最尾要加':'
rain = input('今日有無落雨')
if rain == '有':
	print('帶遮')
	print('買野食')
	print('睇戲')
	if rain == '無':
		print('拜拜')
	else:
		print('走啦你')

age = input('你幾大?')#因為age係字, 3係實數字;不同,計不了,所以要做casting(轉型)
age = int(age)#casting
if age >= 20:
	print('你可以投票')
if age <=20:
	print('你不可以投不票')

age = input('另一個例子:你幾大?')#因為age係字, 3係實數字;不同,計不了,所以要做casting(轉型)
age = int(age)#casting
if age >= 20:
	print('你可以投票')
else:
	print('你不可以投票')


celsius = input('input celsius')
celsius = int(celsius)#or float(for小數)
fahrenheit = celsius * 9 / 5 + 32
print (fahrenheit, 'F')

#else if 另外如果
#and = 而且
age = input('你幾大')
age = int(age)
if age < 13:
	print('初中人')
elif age >= 13 and age <18:
	print('高中人')
elif age >= 18 and age <22:
	print('大學人')
else:
	print('社會人')

height = input('what is your height in kgs?')
height = int(height)
weight = input('what is your weight in meters')
weight = float(weight)

BMI_D = weight / height
BMI_D = int(BMI_D)

BMI = BMI_D / height
if BMI < 18.5:
	print ('過輕')
elif BMI >= 18.5 and BMI < 24:
	print ('正常')
elif BMI >= 24 and BMI < 27:
	print ('過重')
elif BMI >= 27 and BMI < 30:
	print ('輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print ('中度肥胖')
else:
	print('重度肥胖')
print ('Your BMI is', BMI)
print ('Your BMI_D is', BMI_D)

country = input('請問你係咩國家既人?')
age = input('請問你幾歲?')
age = int(age)
if country == 'china':
	if age >= 18:
		print('你可以考車牌')
	else:
		print('你不可以考車牌')

elif country == 'USA':
	if age >= 16:
		print('你可以考車牌')
	else:
		print('你不可以考車牌')