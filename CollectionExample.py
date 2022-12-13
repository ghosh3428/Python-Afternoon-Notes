class Collection:
    def __init__(self):
        self.ar =list()
        self.l = 0

    def acceptSize(self):
        print("Enter the number of elements you want to save : ")
        self.l = int(input())

    def acceptData(self):
        for i in range(self.l):
            print("Enter the number at index",i)
            self.ar.append(int(input()))

    def display(self):
        for i in self.ar:
            print(i , end="\t")
        print()

    def __add__(c1 , c2):
        c = Collection()
        c.ar.extend(c1.ar)
        c.ar.extend(c2.ar)
        for i in c.ar:
            if c.ar.count(i) > 1:
                c.ar.remove(i)
        c.l = len(c.ar)
        c.ar.sort()
        return c

    def __sub__(c1 , c2):
        c = Collection()
        #Finding the common values
        for i in c1.ar:
            if i in c2.ar:
                c.ar.append(i)
        #removing the repeated values
        for i in c.ar:
            if c.ar.count(i) > 1:
                c.ar.remove(i)

        #setting the size
        c.l = len(c.ar)

        #checking and sorting
        if c1.l >= c2.l:
            c.ar.sort()
        else :
            c.ar.sort(reverse = True)

        return c

c1 = Collection()
c2 = Collection()

print("Enter Details of Collection 1")
c1.acceptSize()
c1.acceptData()


print("Enter Details of Collection 2")
c2.acceptSize()
c2.acceptData()

print("Collection 1 :")
c1.display()

print("Collection 2 :")
c2.display()

c3 = c1 + c2
print("Collection 3 after addition :")
c3.display()


c4 = c1 - c2
print("Collection 4 after subtraction :")
c4.display()

