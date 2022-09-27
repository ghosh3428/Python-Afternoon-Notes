#print only consonents

for i in range(ord('A') , ord('Z') + 1 , 1):
    if chr(i) not in "AEIUO":
        print(chr(i))
