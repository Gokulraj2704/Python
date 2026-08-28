'''
#poitive negative zero
a=int(input("enter the number"))
if(a>0):
    print("poitive number")
elif(a<0):
    print("negative")
else:
    print("zero")

#even or odd
a=int(input("enter the number"))
if(a%2==0):
    print("give number is even")
else:
    print("give number is odd")

#print("Give number is divisible by 3 and 5")
a=int(input("enter the number"))
if(a%3==0 and a%5==0):
    print("Give number is divisible by 3 and 5")
else:
    print("Give number not divisible by 3 and 5")

#electricity units consumed
a= int(input("enter the units"))
if a>=0 and a<=100:
    d=a*2
    print(d,"electricity units consumed")
elif a>=101 and a<=2100:
    d=a*3
    print(d,"electricity units consumed")
elif a>=201 and a<=300:
    d=a*5
    print(d,"electricity units consumed")
elif a>=301:
    d=a*7
    print(d,"electricity units consumed")
else:
    print("invalid input")
#multiplication table from 1 to 20.
a=int(input("enter the number"))
for  i in range (1 ,21):
     print(a,"*",i,"=",a*i)

a=int(input("enter the value"))
for i in range(1,a+1):
    for j in range(i):
        print("*",end="")
    print()
        
a= 5
for i in range(1, a+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

#maximum and minimum of the given three numbers

a=int(input("enter the value1"))
b=int(input("enter the value2"))
c=int(input("enter the value3"))
if a>=b and a>=c:
    print(a,"max  value")
elif a<=b and a<=c:
    print(a,"min  value")
if b>=a and b>=c:
    print(b,"max  value")
elif b<=a and b<=c:
    print(b,"min  value")
if c>=b and c>=a:
    print(c,"max  value")
elif c<=a and c<=b:
    print(c,"min  value")
else:
    print("invalid input")


#Check whether the given year is leap year or non leap year

a=int(input("enter the year"))
if a%4==0:
    print("leap year")
else:
    print("not leap year")
#100 and 400
a=int(input("enter the year"))
if a%4==0 and a%100!=0 or a%400==0:#1900 is not leap year
    print("leap year")
else:
    print("not leap year")

# prime number:
a=int(input("enter the value"))
count=0
if a>1:
    for i in range(1,a+1):
        if a%i==0:
            count+=1
if count==2:
     print("prime")
else:
    print("not prime")

#leap or not
a = int(input("enter the year: "))
if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print("leap year")
        else:
            print("not")
    else:
        print("leap year")
else:
    print("not")

'''

