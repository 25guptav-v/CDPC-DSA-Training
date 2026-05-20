rec={}
n=int(input("enter no of students"))
for i in range(n):
  name=input("enter student name:")
  per=float(input("enter perc:"))
  rec[name]=per

print(rec)
for x in rec:
  print(x,"\t",rec[x])