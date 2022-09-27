#print all the factors of a number
# 10
#factors of 10 : 1,2,5,10


#start  : 1
#end    : n
#step   : +1
#code  : n%i == 0

n = int(input("Enter a number :"))

print("Factors of" , n ,"are :")

for i in range(1 , n+1 ):
    if n%i == 0:
        print(i)
