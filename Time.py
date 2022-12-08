class Time:
    def __init__(self):
        self.hrs = 0
        self.min = 0

    def getTime(self,h , m):
        self.hrs = h
        self.min = m
        while(self.min >=60):
            self.hrs = self.hrs + 1
            self.min = self.min - 60

    def printTime(self):
        if self.hrs<10:
            print("0" + str(self.hrs) +":", end="")
        else:
            print(str(self.hrs) +":", end="")

        if self.min<10:
            print("0" + str(self.min))
        else:
            print(self.min)

    def sumTime(self,t1,t2):
        self.min = t1.min + t2.min
        self.hrs = t1.hrs + t2.hrs
        
        while(self.min >=60):
            self.hrs = self.hrs + 1
            self.min = self.min - 60

        return self

    def __eq__(t1 , t2):
        if(t1.hrs == t2.hrs and t1.min == t2.min):
            return True
        else :
            return False

    def __gt__(t1 , t2):
        if(t1.hrs > t2.hrs):
            return True
        elif (t1.hrs < t2.hrs):
            return False
        else:
            if(t1.min > t2.min):
                return True
            else:
                return False

    def __add__(t1 , t2):
        t = Time()
        t.hrs = t1.hrs + t2.hrs
        t.min = t1.min + t2.min

        while(t.min >=60):
            t.hrs = t.hrs + 1
            t.min = t.min - 60

        return t

obj1 = Time()
print("Enter hours and minutes for first time object")
obj1.getTime(int(input()),int(input()))
obj1.printTime()

obj2 = Time()
print("Enter hours and minutes for second time object")
obj2.getTime(int(input()),int(input()))
obj2.printTime()

obj3 = Time()
#obj3 =obj3.sumTime(obj1 , obj2)
obj3 = obj1 + obj2
#obj3 = __add__(obj1 , obj2)
print("Adding the two tiome objects")
obj3.printTime()

if obj1 == obj2:
    print("Both the time objects are equal")
elif obj1 > obj2:
    print("first object is bigger")
else:
    print("second object is bigger")






        
