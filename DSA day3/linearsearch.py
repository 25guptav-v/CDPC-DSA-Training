def linear_search(n, arr, target):
  flag=False
  for i in range(n):
    if target!=arr[i]:
      pass
    else:
      flag=True
      loc=i
  if flag==true:
    print("search is successful and present at ",loc)
  else:
    print("search is successful")

if __name__ == '__main__':
  n = int(input("Enter size: "))
  arr = []
  for i in range(n):
    arr.append(int(input()))
  target = int(input("Enter number to search: "))
  linear_search(n, arr, target)