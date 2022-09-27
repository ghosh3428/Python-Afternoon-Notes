#range(start , end , step)
#start default value is 0
#step default value is 1

for i in range(10):
    ch= input ("Enter a character :")
    #outer if
    if ch.isalpha():
        
        #inner if
        if ch.lower() in"aeiou":
            print(ch,"is a VOWEL.\n")
            
        #else block in inner if
        else:
            print(ch ,"is a CONSONENT\n")
            
    #else block of outer if
    else:
        print("Character is not an alphabet.\n")
