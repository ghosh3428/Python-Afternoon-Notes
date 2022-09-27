#print all uppercase alphabet
#start :ord('A')
#end : ord('Z') + 1
#step : +1
#code : print(chr(i))


#chr() -> converts ascii value to ascii character
#ord() -> converts a acsii character to ascii value

for i in range(ord('A') , ord('Z') + 1 , 1):
    print(chr(i))
