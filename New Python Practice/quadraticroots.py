#find the roots of a quadratic equation

#r1 = -b + sqrt(b^2 - 4ac) / 2a
#r1 = -b - sqrt(b^2 - 4ac) / 2a

# accept values of a , b , c


#input
print("ax^2 + bx + c = 0")

print("Enter the value of 'a' : ")
a = int(input())
print("Enter the value of 'b' : ")
b = int(input())
print("Enter the value of 'c' : ")
c = int(input())


#process
d = (b**2) - (4*a*c)

r1 = (-b + (d**(1/5))) / (2*a)
r2 = (-b - (d**(1/5))) / (2*a)


#output
print("Root 1 =" , r1)
print("Root 2 =" , r2)



