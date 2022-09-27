basic = int(input("Enter basic salary : \n"))

hra = 0
da = 0
gross = 0

if(basic<=10000):
    hra = basic*20/100
    da = basic*80/100
    
elif(basic<=25000):
    hra = basic*25/100
    da = basic*90/100
    
else:
    hra = basic*30 /100
    da = basic*95/100

gross = basic + hra + da

print("---------------SALARY SLIP--------------")
print("Basic   : Rs" , basic)
print("HRA    : Rs" , hra)
print("DA      : Rs" , da)
print("Gross  : Rs" , gross)
print("--------------------------------------------")

