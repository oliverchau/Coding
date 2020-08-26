
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
start = input('請決定數字值範圍(開始值)')
end = input('請決定數字值範圍(結束值)')
start = int(start)
end = int(end)
r = random.randint(start, end) #1-100抽一個數, (start&end係人地決定)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請估數字: ')
	num = int(num)
	if num == r:
		print ('你估中了!')
		print('今次你估第', count, '次')
		break
	elif num > r:
		print ('估細啲啦!')
	elif num < r:
		print ('估大啲啦!')
	print('今次你估第', count, '次')

#List
a = [] #空List
a = [True, 'Toyota', 'Honda', 1132]#「索引」index 0 is True...etc.
print (a[3])
a.append('Audi')#'.'=的, append ~= attach sth on it.
print (a)
print(len(a))#len=length of a[]
print('Audi' in a) #是非題**asking the computer yes/no.
print('Benz' in a) #是非題**asking the computer yes/no.

#for loop=將Cars(list) 既野一樣一樣拎出黎。每次拎出黎既野個'暫時名'=car.
cars = ['Toyota', 'Honda']
for car in cars:
	print(car)#每次拎一樣野出黎, 就print一次;2樣野=走2次。

names = ['Allen', 'Tom', 'Mayday', 'JJ', 'Jolin', 'Jay', 'Jam']
for name in names:
	print('Hi', name)

#字串當清單
car = 'Audi'
for c in car:
	print(c)
print(len(car))
print('A' in car)

#讀取檔案 (係同一路徑起左個新既file先, 再叫佢做food.txt)
with open('food.txt', 'r') as f:
	for line in f:#每一行叫line;一行行咁print出黎
		print(line)#首先,txt你enter左一次=1*\n(換行), 然後print本身又換一次行
		#變左換左行
data = []
with open('food.txt', 'r') as f:
	for line in f:#每一行叫line;一行行咁print出黎
		data.append(line)#今次就無左換行,但見到個\n。
print(data)

data = []
with open('food.txt', 'r') as f:
	for line in f:#每一行叫line;一行行咁print出黎
		data.append(line.strip())#去掉[line]多餘的東西;空格,行...etc.*(只能對字串有效)
print(data)

#open 是打開(夾住)檔案
#以前就要右 close.
#但with 就可以簡化close, 只要當程式離開了with的structure(e.g line:221)
data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1#if count = count + 1
		if count % 1000 == 0:#%=求餘數
			print(len(data))#每睇一下印一次
print(len(data))	

print(data[0])
print('---------------------')
print(data[1])