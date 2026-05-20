arr=[5,66,84,2,5,8,99]
min=0                             #decending order
loc=0
for i in range(len(arr)-1):
    min=arr[i]
    loc=i
    for j in range(i+1,len(arr)):
      if min<arr[j]:
        min=arr[j]
        loc=j
        arr[i],arr[loc] = arr[loc],arr[i]
print(*arr)