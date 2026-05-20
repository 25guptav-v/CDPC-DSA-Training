no=int(input("enter no: "))
sum=0
save=no
fact=1
while no>0:
    rem=no%10
    fact=1
    while rem>0:
        fact=fact*rem
        rem=rem-1
        sum=sum+fact
        no=no//10
        print(fact)
if save==sum:
        print("is peterson")
else:
        print("is not peterson")