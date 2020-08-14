
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

height = input('what is your height in centimeters cms?')
height = int(height)
weight = input('what is your weight in kgs?')
weight = int(weight)

BMI = weight / height / height * 100 * 100
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

country = input('請問你係咩國家既人?')
age = input('請問你幾歲?')
age = int(age)
if country == 'China':
	if age >= 18:
		print('你可以考車牌')
	else:
		print('你不可以考車牌')

elif country == 'USA':
	if age >= 16:
		print('你可以考車牌')
	else:
		print('你不可以考車牌')
else:
	print('你只能輸入China or USA')

while True:
	mode = input('請輸入遊戲模式: ')
	if mode == 'q': # quit
		break
	elif mode == '1':
		print('Gaming mode 01 activated')
	elif mode == '2':
		print('Gaming mode 02 activated')
	else:
		print('只能輸入 1/2/q')
#control c = force shutdown of the program
while True:
	mode = input('請輸入你的名字: ')
	if mode == 'q': # quit
		break
#實際執行起來的話，只會印出第一次a以後，就卡在印b的地方無限迴圈，所以c沒有機會印出來	
#i = 0
#while i < 100:
    #print('a')
    #j = 0
    #while j < 100:
    	#print('b')
#print('c')

#這要仔細思考雙層的while, while j < 100的那個迴圈因為在while i < 100的迴圈裡，
#整個迴圈會執行100次，裡面又會印出100次b，所以變成100*100 = 印出10000次b
#i = 0
#while i < 100:
    #print('a')
    #j = 0
    #while j < 100:
        #print('b')
        #j = j + 1
    #i = i + 1
#print('c')
#i=0, i=1,=2, i=2,=3
i = 0
while i < 6:
    print('a')
    i = i + 1


print ('密碼重試程式')
n = 3
while True:
	password = input('請輸入密碼: ')
	if password == '123456':
		print ('登入成功!')
		break
	else:
		print ('密碼錯誤,請重新輸入,你還有', n,'次機會')
		n = n - 1
		if n == 0:
			print ('你已沒機會了,拜拜~')
			break

#載入一個叫random的資料庫(package)中的一本「書」/module, '.'=random(module)中的randon int.(整數)
import random
r = random.randint(1, 100) #1-100抽一個數
while True:
	num = input('請估數字: ')
	num = int(num)
	if num == r:
		print ('你估中了!')
		break
	elif num > r:
		print ('估細啲啦!')
	elif num < r:
		print ('估大啲啦!')