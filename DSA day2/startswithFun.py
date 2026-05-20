no=input("enter mobile number")
if no.isdigit():
  if len(no)==10:
    if no.startswith('6') or no.startswith('7'):
     print("Valid mobile number.")
    else:
     print("Mobile number should start with 6 or 7.")
  else:
    print("Please enter 10 digits only.")
else:
  print("Please enter a number in digit format only.")