#accept 20 number and print the sum of even and odd number
#1,2,3,4,5,6,7,8,9,10
#even sum = 30
#odd sum = 25
evensum =0
oddsum=0
for i in range(10):
    n=int(input("Enter a number"))
    if n%2==0:
        evensum=evensum+n 
    else:
        oddsum=oddsum+n

print("Even sum :" , evensum)
print("Odd Sum  :" , oddsum)
        
