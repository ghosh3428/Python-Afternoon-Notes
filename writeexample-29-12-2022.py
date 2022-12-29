class PhoneDirectory:
    def __init__(self):
        self.name = ""
        self.phone =""

    def acceptData(self):
        self.name = input("Enter User Name : ")
        self.phone = input("Enter Phone Number : ")

        fo = open("phone.txt","a")
        fo.write("\n")
        fo.write(self.name)
        fo.write("\t")
        fo.write(self.phone)

        fo.close()
        print("Data saved successfully")

        
    def displayData(self):
        fo = open("phone.txt" ,"r")
        
        data = fo.readlines()

        print(data)

        fo.close()

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
            print("Data not Found")

        fo.close()

ph = PhoneDirectory()

ph.searchData()
