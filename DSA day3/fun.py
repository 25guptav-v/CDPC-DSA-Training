def add(a, b):     # Function with parameter and return with multiple value
  res1=a+b
  res2=a-b
  res3=a*b
  res4=a/b
  return res1,res2,res3,res4
  
if __name__ == '__main__':
  a=int(input("enter a: "))
  b=int(input("enter b: "))
  r1,r2,r3,r4= add(a,b)
  print("Add is ",r1)
  print("Sub is ",r2)
  print("Mul is ",r3)
  print("Div is ",r4)