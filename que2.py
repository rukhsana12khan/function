
(2)
def function(a,b,c=5):
	d=a+b+c
	print("addition=",d)
function(5,7)


(3)
def function(a,b):
	d=a+b
	return d
x=int(input("enter"))
y=int(input("enter"))
z=function(x,y)
print("addition=",z)


(4)
def add():
	a=int(input("enter"))
	b=int(input("enter"))
	c=a+b
	return c
s=add()
print(s)



(5)
def add(number):
	if number ==2:
		pass
	else:
		print("number=",number)
add(3)
add(2)


(6)
def ask():
	print("who is the founder of facebook ?")
	print("mark zuckerberg")
	print("bill gates")
	print("steve jobs")
	print("larry page")
ask()
ask()
ask()
ask()
ask()


(7)
def ask():
	i=0
	while i<7:
		i=i+1
		print("who is the founder of facebook ?")
		print("mark zuckerberg")
		print("bill gates")
		print("steve jobs")
		print("larry page")
ask()



(8)
def ask(list):
	b=max (list)
	print(b)
ask([3,5,7,34,2])


(9)
def ask(list):
	i=0
	sum=0
	while i<len(list):
		sum=sum+list[i]
		i=i+1
	print(sum)		
ask([1,2,3,5,4,5])


(10)
def function():
	i=1
	while i<=1000:
		j=i
		sum=0
		m=1
		while m<i:
			if j%m==0:
				sum=sum+m
			m=m+1
		if sum==j:
			print('perfect',j)
		i=i+1
function()



(11)
def function():
	sum=n1+n2+n3
	avrage=sum/3
	print(avrage)
n1=int(input('enter'))
n2=int(input('enter'))
n3=int(input('enter'))	
function()



(12)
def function(limit):
	i=0
	while i<=(limit):
		if i%2==0:
			print('even=',i)
		else:
			print('odd=',i)
		i=i+1
function(3)



(13)
def function(limit):
	i=0
	sum=0
	sum1=0
	sum2=0
	while i<=(limit):
		if i%3==0 and i%5==0:
			sum=sum+i
		if i%3==0:
			sum1=sum1+i
		elif i%5==0:
			sum2=sum2+i
		i=i+1
		total=sum+sum1+sum2
	print(total)
function(10)



(14)
def function(speed):
		if speed <=70:
			print("Ok")
		elif speed>=70:
			user=speed-70
			point=user/5
			print(point)
			if point>12:
				print(point,"licence suspent")
function(135)



(15)
def square(y):
	i=1
	while i<=y:
		print(i,':',i*i,end=" , ")
		i=i+1
square(20)





# (DOCKQUESTION)


(1)
def function(list):
		count=0
		for i in list:
			if len(i)>1 and i[0]==i[-1]:
				count=count+1
		print(count)
function(list(['abc','xyz','aba','1221']))



(2)
def fuction(list):
	i=0
	max=0
	smax=0
	thmax=0
	while i<len(list):
		if list[i]>max:
			thmax=smax
			smax=max
			max=list[i]
		if list[i]<smax and list[i]>smax:
			smax=list[i]
		i=i+1
	print("first",max)
	print("second",smax)
	print("third",thmax)
fuction(list([50,34,55,70,80,63,12,5,10,7]))


(3)
def function(list):
	i=0
	sum=0
	while i<len(list):
		sum=sum+list[i]
		i=i+1
	print(sum)
function(list([8,2,3,0,7]))



(4)
def function(list):
	i=-1
	while i>=-len(list):
		print(list[i],end="")
		i=i-(1)
function(list("1234abcd"))



(5)
def function(list):
	i=0
	m=[]
	while i<len(list):
		if list[i] not in m:
			m.append(list[i])
		i=i+1
	print(m)
function(list([1,2,3,3,3,3,4,5]))


(6)
def function(list):
	i=0
	m=[]
	while i<len(list):
		if list[i]%2==0:
			m.append(list[i])
		i=i+1
	print(m)
function(list([1,2,3,4,5,6,7,8,9]))


(7)
def function():
	if bmi<=18.5:
		print("underweigjt")
	elif bmi>=18.5 and bmi<=25.0:
		print("normal")
	elif bmi>=25.0 and bmi<=30.0:
		print("overweight")
	else:
		print("obese")
bmi=float(input('enter'))
function()



(10)
def function():
	a=input('enter')
	b=input('enter')
	sum=int(a)+int(b)
	print('"',a,'"',',','"',b,'"','-->','"',sum,'"')
function()




(13)
def prime():
	count=0
	i=1
	while a>=i:
		if a%i==0:
			count=count+1
		i=i+1
	if count==2:
		print('prime')
	else:
		print('not prime')
a=int(input('enter'))
prime()




(14)
n=int(input('enter'))
def prime():
	i=1
	count=0
	while i<=n:
		if n%i==0:
			count=count+1	
		i+=1
	if count==2:
		print('prime n=',n)
	else:
		print("composit n=",n)
prime()


(16)
def table():
	i=1
	while i<=10:
		print(a,'*',i,'=',i*a)
		i=i+1
a=int(input('enter'))
table()



(17)
def function():
	if age>=18:
			print('ileigible for vote')
	else:
			print('not ileigible')
age=int(input('enter'))
function()



(25)
def function(list):
	i=0
	pos=0
	neg=0
	while i<len(list):
		if list[i]>=0:
			pos=pos+1
		elif list[i]<=0:
			neg=neg+1
		i=i+1
	print('positive=',pos)
	print('negative=',neg)
function(list([2,-7,5,-64,-14]))



(26)
def function():
	if a%5==0 and a%3==0:
		print('fizz buzz')
	elif a%3==0:
		print('fizz')
	elif a%5==0:
		print('buzz')
	else:
		print('number=',a)
a=int(input('enter'))
function()



(30)
def prime(limit):
	i=1
	while i<=limit:
		b=1
		count=0
		while b<=i:
			if i%b==0:
				count=count+1
			b=b+1
		if count==2:
			print('prime',i)
		i=i+1
prime(100)



# (Recursion)

(1)
def xyz(s,n):
	if n==0:
		print(s[0])
	else:
		print(s[n],end="")
		xyz(s,n-1)
s=input('enter')
xyz(s,len(s)-1)



(2)
def dis(str):
	def show():
		return "show function"
	result= show()+  str +" dis function"
	return result
a=dis("greeky shows")
print(a)


(3)
def function(a,b):
	c=a+b
	return c
def done():
	d=function(5,7)+50
	return d
print(done())



(4)
def table(n):
	print(n)
	if n==10:
		return 1
	return table(n+1)
n=int(input("enter a number"))
table(n)



(5)
def table(n):
	print(n*2)
	if n==10:
		return 1
	return table(n+1)
n=int(input("enter a number"))
table(n)



()