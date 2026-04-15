# 13. Write a program to print numbers from 1 to 50 using a loop.
print("First 50 natural numbers...")
for i in range(1,51):
    print(i)


# 14. Write a program to print the multiplication table of a number.
i = 1
while(i<=10):
    print(f"{i} * 2 = {i*2}")
    i+=1


# 15. Write a program to calculate the sum of numbers from 1 to 100.
ans = 0
for i in range(1, 101):
    ans += i


# 16. Write a program to print the factorial of a number.
fac = 1
num = int(input("Enter a number: "))
for i in range(1, num):
    fac*=i
print(f"Factorial of {num} is {fac}")