a="Learning python is very easy from ashish sir"
ls=a.split()
print(ls)
ans="" # Initialize ans
for x in ls:
  ans=ans+x[::-1]+" "
print(ans)