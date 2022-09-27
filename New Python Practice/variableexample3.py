print("Enter Student Name :")
name =input()

roll_number = input("Enter Student Roll Number :\n")

phy = int(input("Enter Physics Marks :\n"))
che = int(input("Enter Chemistry Marks :\n"))
bio = int(input("Enter Biology Marks :\n"))

total = phy + che + bio

average_marks = total / 3

passed = input("Enter if the student have passed(True/False) :\n")


print("Student Name  :" ,name)
print("Roll Number     :" ,roll_number)
print("Average Marks :" ,average_marks)
print("Passed            :" ,passed) 
