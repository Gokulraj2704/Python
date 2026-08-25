'''
#1
mark1 = int(input("enter the mark1"))
mark2 = int(input("enter the mark2"))
mark3 = int(input("enter the mark3"))
average_mark = mark1+mark2+mark3/3
print(average_mark)
if average_mark >150 and average_mark<=300:
    
    print("student is eligible for admission")
else:
    print("student is not eligible for admission")


2
salary = int(input("enter the salary"))
experience = int(input("ENTER experience"))
rating = int(input("enter rating"))
if experience>=5 and experience<=10:
    if rating==5:
        bonus=salary*0.25
        print(bonus)
elif rating==4:
    bonus=salary*0.2
    print(bonus)
else:
    print("not eligible")


user_name="Gokul Raj"
password="go12345"
otp="4569"
user=input("enter the user_name:")
passwordin=input("enter the password:")
otp=input("enter the otp")
if user_name==user and password==passwordin and otp==otp:
    print("login")
else:
    print("incorrect")
3
purchase_amount= float(input("enter the amount"))
membership=input("enter the  yes/no")
if purchase_amount>500 and purchase_amount<=1000:
        discount_amount=(purchase_amount*(10/100))
        final_amount=purchase_amount-discount_amount
        print(final_amount)
elif purchase_amount>1001 and purchase_amount<=5000:
    discount_amount=(purchase_amount*20/100)
    final_amount=purchase_amount-discount_amount
    print(final_amount)
else:
        print("no discount")

if membership=="yes" and final_amount>1000:
    festival_offer=(final_amount*(5/100))
    f_amount= final_amount-festival_offer
    print(f_amount)
else:
    print("not")
8
my=input("enter the setences")
word= input("enter the  word")
if word in my:
    print("word in the setences")
else:
    print("Not in the setences")
''''

