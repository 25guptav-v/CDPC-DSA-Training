class Student:
   def  __init__(self):
    print("default constructor")
   def  __init__(self,a):
    print(a)
   def  __init__(self,a,b):
      print(a,b)

   def show(self):
    print("I am in showA")
s=Student(11,12);
s.show();