#Write a C program to input any character and check whether it is alphabet, digit or special character.data = input("Enter a character")
data =input("enter a character")
if data.isalpha():
   print("character is an alphabet")
elif data.isdigit():
    print("character is a digit")
else:
    print("character is a spacial character")
    
    
