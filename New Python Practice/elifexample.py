age = int(input("Enter your age : "))

#if ....elif
if age>0 and age<=5:
    print("I Am INFANT.")
elif age>5 and age<=12 :
    print("I Am CHILD")
elif age>12 and age<=19:
    print("I Am TEENAGER")
elif age>19 and age<=59 :
    print("I Am ADULT")
elif age>59:
    print("I Am OLD")
