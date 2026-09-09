#q1
'''
a=int(input("enter the number "))
if a>0:
    print("Positive")
elif a<0:
    print("negative")
else:
    print("zero")

#q2
n1=int(input("n1:"))
n2=int(input("n2:"))
n3=int(input("n3:"))
if(n1>n2 and n1>n3):
    print(n1," is largest")
elif(n2>n1 and n2>n3):
    print(n2," is largest")
elif(n3>n1 and n3>n2):
    print(n3," is largest")
else:
    print("invalid")

#q3
a=int(input("enter the value"))
for i in range(1,21):
       print(a,"*",i,"=",a*i)

#q4
a=int(input("enter the year"))
if(a%4==0 and a%100!=0 or a%400==0):
    print("leap year")
else:
    print("not leap")
 
#q5
s1=int(input("s1:"))
s2=int(input("s2:"))
s3=int(input("s3:"))
if(s1>=45  and s<=100):
    print(s1," is passed")
else:
    print("try again")
if(s2>=45cc):
    print(s2," is passed")
else:
    prinr("try again")
if(s3>=45  and s<=100):
    print(s3," is passed")
else:
    print("try again")
'''
'''
for i in range(1,10):
    s=int(input("enter the mark"))
    if(s>=45 and s<=100):
        print(s,"student" +str(i) +" is passed")
    else:
        print("try again")
'''
'''
#q6
username="Gokul45"
password="GR@4507"
a=input("enter the username:")
b=input("enter the password")
if a==username and b==password:
    print("login")
else:
    print("invalid")
'''
'''
#q7
n=int(input("enter the number:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
#q8
for i in range(1,21):
 if i%3==0:
     continue
 print(i)

#q9
n=int(input("enter the number"))
fact=1
for i in range(1,n+1):
      fact=fact*i
print(fact)

#q10
count=0
for i in range(1,51):
 if i%2==0:
     count+=1
print(count)
#q11

str1=str(input("enter the sentences:"))
a=0
c=0
for i in (str1):
    if i in "aeiouAEIOU":
        a+=1
    elif i.isalpha():
        c+=1
print(str1,"vowels ",a)
print(str1,"consonants ",c)

#q12 and q13
s=input("enter the word")
rev=""
for i in s:
    rev = i+rev
print(s,rev)
if(s==rev):
    print("palindrome")
else:
    print("not palindrome")
#q14
a=input("Enter the sentences")
b=input("enter the word")
count=0
for i in a.split():
    if i == b:
        count +=1
print(b,count)
#q15
a=input("Enter the sentences")
b=""
for i in a.split():
    if len(i)>len(b):
          b=i
print(b)
#q16
s = input("Enter: ")
s = s.replace(" ", "-")
print(s)

#q17
s = input("Enter string: ")
d = 0
l = 0
sp = 0
for i in s:
    if i.isdigit():
        d += 1
    elif i.isalpha():
        l += 1
    else:
        sp += 1
print("Digits ", d)
print("Letters", l)
print("Special ", sp)

#q18
a=[50,45,47,80,90]
lag=a[0]
small=a[0]
for i in a:
    if  i>lag:
        lag=i
        
    if  i<small:
        small=i
print(lag)
print(small)

#q19
n=int(input("enter the range"))
a=[]
c=[]
for i in range(n):
    b=int(input("enter the value"))
    a.append(b)
    print(a)
for i in a:
    if i not in c:
        c.append(i)
print (c)
#20
a=[10, 20, 30]
b=[40, 50, 60]
c=a+b
print(c)

#21
a=[]
for i in range(1, 11):
    a.append(i ** 3)
print(a)

#q22
a=[50, 20, 80, 10, 40]
a.sort()
print(a)
a.sort(reverse="0")
print(a)

a=[10, 20, 30, 40, 50]
total = 0
for i in a:
    total = total + i
average = total / len(a)
print(total)
print(average)

a=[10, 50, 30, 80, 40]
a.sort()
print(a[-2])

a=(10, 20, 30)
b=(40, 50, 60)
c=a + b
print(c)

a=(10, 20, 30, 40, 50)
print(a[1])
print(a[3])

a=(10, 20, 30, 40, 50)
if 30 in a:
    print("Element in")
else:
    print("not")

a=(10, 50, 30, 80, 40)
print(len(a))
print(max(a))
print(min(a))
'''
a=(10, 20, 30, 40)
b=list(a)
print(b)
c=tuple(b)
print(c)
