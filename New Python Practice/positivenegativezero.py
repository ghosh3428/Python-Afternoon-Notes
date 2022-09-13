#Write a C program to check whether a number is negative, positive or zero.

first = int(input("Enter a number : "))

if first == 0:
    print("Number is zero")
elif first<0:
    print("Number is negative")
else:
    print("Number is positive")
