no=int(input("enter no: "))
sum=0
save=no

count=len(str(no))

while no>0:
    rev=no%10
    summ=sum+(rev**count)
    no=no//10

if rev==save:
      print("no is armstrong")
else:
      print("no is not armstrong")