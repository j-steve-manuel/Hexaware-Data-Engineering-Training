# 9. Write a program to check whether a number is even or odd.
num = int(input("Enter a number"))
if(num%2==0):
    print("It's an evem number")
else:
    print("It's an odd number")


# 10. Write a program to check whether a number is positive or negative .
num = int(input("Enter a number"))
if(num>0):
    print("Positive Number")
elif(num==0):
    print("Zero")
else:
    print("Negative Number")


# 11. Write a program to check whether a person is eligible to vote (age ≥ 18) .
age = int(input("Enter your age:"))
if(age>=18):
    print("You're eligible to vote...")
else:
    print("Your'e too young, chap...")


# 12. Write a program that takes marks as input and prints grade:
marks = int(input("Enter your marks:"))

if(marks>=90):
    print("Grade A")
elif(marks>=70):
    print("Grade B")
elif(marks>=50):
    print("Grade C")
else:
    print("Better Luck Next Time!!!")



