#input
print("Enter Physics marks : ")
phy =int(input())
print("Enter Chemistry marks : ")
che =int(input())
print("Enter Biology marks : ")
bio =int(input())


#process
total = phy + bio + che
percentage = round(total / 3 , 2)


#output
print("------------------MARKSHEET---------------")
print("Physics Marks     :" , phy)
print("Chemistry Marks :" , che)
print("Biology Marks     :" , bio)
print("Percentage         :" , percentage)

if percentage >=50:
    print("You have Passed the exam.")
else:
    print("You have failed the exam.")
print("--------------------------------------------------")
