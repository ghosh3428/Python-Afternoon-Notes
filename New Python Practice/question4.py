#input
phy=int(input("Enter Physics marks :"))
chem=int(input("Enter Chemistry marks:"))
bio=int(input("Enter Biology marks:"))
math=int(input("Enter Mathematics marks:"))
comp=int(input("Enter Computer marks:"))


#process
total_marks=phy+chem+bio+math+comp
percentage=round((total_marks/500)*100 , 2)

if percentage >= 90:
    grade = "A"
elif  (80<=percentage<90) :
    grade = "B"
elif  (70<=percentage<80) :
    grade = "C"
elif  (60<=percentage<70) :
    grade = "D"
elif  (40<=percentage<60) :
    grade = "E"
else:
    grade ="F"


#output
print("---------------MARKSHEET--------------")
print("Physics Marks     :" , phy)
print("Chemistry Marks :" , chem)
print("Biology Marks     :" , bio)
print("Computer Marks :" , comp)
print("Maths Marks       :" , math)
print("Total Marks        :" , total_marks)
print("Percentage         :" , percentage)
print("Grade                :" , grade)
print("------------------------------------------")
    
