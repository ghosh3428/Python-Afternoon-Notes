class Matrix:
    def __init__(self):
        self.ar =list()
        self.r = 0
        self.c = 0
    def acceptSize(self):
        print("Enter the number of rows : ")
        self.r = int(input())
        print("Enter the number of column : ")
        self.c = int(input())

    def acceptData(self):
        for i in range(self.r):
            myli = list()
            for j in range(self.c):
                print("Enter the number at index",i,",",j)
                myli.append(int(input()))
            self.ar.append(myli)

    def display(self):
        for i in range(self.r):
            for j in range(self.c):
                print(self.ar[i][j] , end="\t")
            print()

    

m1 = Matrix()

print("Enter Details of Collection 1")
m1.acceptSize()
m1.acceptData()
m1.display()



