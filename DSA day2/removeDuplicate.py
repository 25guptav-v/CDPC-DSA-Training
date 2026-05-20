a="ABCDABBCDABBBCCCDDEEEF"
ans=""
for i in a:
  if i not in ans:
    ans=ans+i
print(ans)