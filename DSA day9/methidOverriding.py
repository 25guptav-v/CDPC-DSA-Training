class Parent:
    def __name__(self):
        self.speed=100
        print("cash,gold")
    def bike(self):
        print("splender+ ",self.speed)

class Child(Parent):
    def __init__(self):
        self.speed=120
    def bike(self):
        print("HB",self.speed)
obj=Child()
obj.bike()