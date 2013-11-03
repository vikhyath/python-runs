class TestClass:
    x = None
    y = 0
    def __init__(self, val):
        self.x = val
        TestClass.y += 1
    def printbasemeth(self):
        print 'x is',self.x
        print 'y is',TestClass.y
    @staticmethod
    def staticmeth(x):
        print x + TestClass.y

class NewTestClass(TestClass):
    def __init__(self, val):
        TestClass.__init__(self, val)

obj = TestClass(5)
obj.printbasemeth()
TestClass.staticmeth(obj.x)

objnew = NewTestClass(6)
objnew.printbasemeth()
NewTestClass.staticmeth(objnew.x)

#### Output ####

# x is 5
# y is 1
# 6
# x is 6
# y is 2
# 8