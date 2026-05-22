class A:
    def showA(self):
        print("I am in Class A")
class B():
    def showB(self):
        print("I am in Class B")
class C(A,B):
    def showC(self):
        print("I am in Class C")

if __name__ == '__main__':
    obj=C()
    obj.showA()
    obj.showB()
    obj.showC()