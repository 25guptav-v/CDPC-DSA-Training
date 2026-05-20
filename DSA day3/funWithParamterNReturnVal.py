def add(a, b):     # Function with parameter and return value
  res=a+b
  return res

if __name__ == '__main__':
  a=int(input("enter a: "))
  b=int(input("enter b: "))
  r= add(a,b)
  print("Addition is ",r)