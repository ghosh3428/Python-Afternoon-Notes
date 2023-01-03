class PhoneDirectory:
    def __init__(self):
        self.name = ""
        self.phone =""

    def acceptData(self):
        self.name = input("Enter User Name : ")
        self.phone = input("Enter Phone Number : ")
        fo = open("phone.txt","a")
        fo.write(self.name)
        fo.write("\t")
        fo.write(self.phone)
        fo.close()
        print("Data saved successfully.\n")

        
    def displayData(self):
        fo = open("phone.txt" ,"r")
        data = fo.readlines()
        for i in data:  
            print(i ,end="")
        fo.close()
        print("\n")

    def searchData(self):
        fo = open("phone.txt" , "r")
        name = input("Enter the name you want to search : \n")
        found = False
        data = fo.readlines()
        for i in data:
            row = i.split("\t")
            if name.upper() in row[0].upper():
                print(row)
                found = True

        if found == False:
            print("Data not Found.\n")

        fo.close()


    def deleteData(self):
        fo = open("phone.txt" , "r")
        name = input("Enter the name you want to delete : \n")
        found = False
        data = fo.readlines()
        for i in data:
            row = i.split("\t")
            if name.upper() in row[0].upper():
                data.remove(i)
                found = True
                break    
        if found == False:
            print("Data not Found.\n")
        else:
            print("Data Deleted Successfully.\n")
        fo.close()

        fo = open("phone.txt","w")
        for i in data:
            fo.write(i)
        fo.close()

    def updateData(self):
        fo = open("phone.txt" , "r")
        data = fo.readlines()
        fo.close()

        name = input("Enter the name you want to update : \n")
        found = False

        for i in range(0,len(data),1):
            if name in data[i]:
                print("Enter new name")
                nn = input()
                print("Enter new phone number")
                ph = input()
                data[i] = nn +"\t"+ph+"\n"
                found = True
                
        if found == False:
            print("Data not Found.\n")
        else:
            print("Data Updated Successfully.\n")
        fo.close()

        fo = open("phone.txt","w")
        for i in data:
            fo.write(i)
        fo.close()

    def menu(self):
        while(True):
            print("--------------PHONE MENU-----------")
            print("1. Add")
            print("2. Display")
            print("3. Search")
            print("4. Delete")
            print("5. Update")
            print("0. Exit")
            print("-----------------------------------")

            ch = int(input())
            if ch == 0:
                print("\n\nTHANK YOU\n\n")
                break
            elif ch == 1:
               self.acceptData()
            elif ch == 2:
               self.displayData()
            elif ch == 3:
               self.searchData()
            elif ch == 4:
               self.deleteData()
            elif ch == 5:
               self.updateData()
            else:
               print("\nInvalid Input\n") 
        

ph = PhoneDirectory()
ph.menu()
