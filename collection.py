class Collection:
    def __init__(self,l):
        self.ar = list()
        self.len = l

    def input(self):
        print("Enter " + str(self.len) +" numbers:")
        for i in range(self.len):
            self.ar.append(int(input()))

    def  display(self):
        print("Collection Elements : " )
        for i in self.ar:
            print(i , end="\t")
        print()

    def common(self,c1):
        c = Collection(0)
        for i in self.ar:
            if i in c1.ar:
                c.ar.append(i)

        return c

print("Collection1")
obj1 = Collection(10)
obj1.input()
obj1.display()


print("Collection2")
obj2 = Collection(5)
obj2.input()
obj2.display()


print("Common")
obj3 = obj1.common(obj2)
obj3.display()


        
