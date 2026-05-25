import re
list=re.split(",","Ashish,Amar,neha,Gaurav,Aditya,Alisha,Devyani")
print(list)
for x in list:
    print(x)

l=re.split("\\.","www.help4code.com")
print(l)
for x in l:
    print(x)

s="ashish$sir$python"
l=s.split("$")
print(l)