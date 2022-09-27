#Single line Sequence -> " " , ' '
#multiple line sequence -> ''' ''' , """ """

first_name = "Amit"
last_name = 'Kumar'
address='''Flat No.2 ,
Abc Appartment,
xyz road,
jadavpur , kolkata
west bemgal - 700032'''

print(first_name + " " +  last_name)
print("-----------------------")
print(address)



#Functions
#upper()
#lower()
#capitalize()

#isupper()
#islower()
#isalpha()
#isdigit()
#isspace()

#find(char) -> finds the index position of the first
#                    occurence of the character
#                   if not found then returns -1

print("-----------------------------")
name = "Niit Jadavpur"
print("Index of 'a' is :",name.find("a")) #returns 6

#count()  -> finds the frequency of a str
print("---------------------------------")
print("Frequency of 'a' is :", name.count('a'))

#len()      -> total number of character in a sequence
print("---------------------------------")
print("Length is :",len(name))

#operator
# + -> joining
# * -> replication

print("----------------------------")
print(("Niit" + " " )* 3)

#add data to sequence -> data gets added at the last position
# +
print("---------------------------------")
name = "Niit" + " Kolkata"
print(name)
