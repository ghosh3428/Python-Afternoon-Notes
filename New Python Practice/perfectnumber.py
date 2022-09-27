#check if a number is a perfect number
# 6 -> 1 + 2 + 3 = 6
#sum = 0
#start  : 1
#end    : n
#step   : +1
#code  : n%i == 0
#               SUM = SUM + I

#IF SUM == N
            

n = int(input("Enter a number :"))
mysum = 0
for i in range(1 , n ):
    if n%i == 0:
        mysum = mysum + i

if mysum == n:
    print(n,"is a perfect number.")
else :
    print(n,"is not a perfect number.")
