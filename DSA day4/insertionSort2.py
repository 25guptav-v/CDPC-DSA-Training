arr=[5,66,84,2,5,8,99]
currenr=0
pos=0
for i in range(len(arr)-1):
  current=arr[i]
  pos=i
  while current>arr[pos-1] and pos>0:
    arr[pos]=arr[pos-1]
    pos=pos-1
  arr[pos]=current
print(*arr)


