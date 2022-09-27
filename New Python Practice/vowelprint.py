#print only vowel

for i in range(ord('A') , ord('Z') + 1 , 1):
    if chr(i) in "AEIUO":
        print(chr(i))
