def binary_search(n, arr, target):
  flag=False
  low=0
  high=n-1
  while low<=high:
    mid=(low+high)//2
    if target!=arr[mid]:
      flag=True
      loc=mid
      break;
    elif flag==true:
      print("search is successful and present at ",loc)
  else:
    print("search is successful")

if __name__ == '__main__':
  n = int(input("Enter size: "))
  arr = []
  for i in range(n):
    arr.append(int(input()))
  target = int(input("Enter number to search: "))
  binary_search(n, arr, target)