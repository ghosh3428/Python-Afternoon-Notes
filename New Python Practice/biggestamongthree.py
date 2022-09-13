#print the biggest value among three numbers

first = int(input("Enter first number : "))
second = int(input("Enter second number : "))
third = int(input("Enter third number : "))


if first == second == third:
    print("All are same.")
elif first > second and first > third:
    print("First is the bigger value.")
elif second>first and second>third:
    print("Second is the bigger value.")
else:
    print("third is the bigger value.")
