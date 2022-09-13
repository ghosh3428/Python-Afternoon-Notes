#print the biggest value among two numbers

first = int(input("Enter first number : "))
second = int(input("Enter second number : "))

if first == second:
    print("Both are same.")
elif first > second:
    print("First is the bigger value.")
else:
    print("Second is the bigger value.")
