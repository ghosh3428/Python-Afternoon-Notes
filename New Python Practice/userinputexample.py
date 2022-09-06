#accept two numbers from user and print the all the arithemetic operation 

#input

#dynamic data : data which is accept at run time

#input() -> which accepts a data at run time in str(character) datatype

#int() -> type conversion function
#converts a str data into an int data

#float() -> type conversion function
#converts a str data into a float data

#str() -> type conversion function
#converts a number data into str data

print("Enter first number")
first = int(input())

print("Enter second number")
second =int(input())

print("Datatype of first :" ,type(first))


#process and output
print("Addition of the numbers is                  :",(first + second))
print("subtraction of the numbers is              :",(first - second))
print("multiplication of the numbers is           :",(first * second))
print("Complete division of the numbers is     :",(first / second))
print("Integer division of the numbers is        :",(first // second))
print("Modulas(Remainder) of the numbers is :",(first % second))
print("Power of the numbers is                      :",(first ** second))
