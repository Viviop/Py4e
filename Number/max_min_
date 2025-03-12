largest = -1
smallest = None
while True:
    num =input("Enter a number: ")
    if num=="done":
       break
    try:
     num=int(num)
     if num>largest :
       largest=num
     if smallest is None:
        smallest=num
     elif smallest>num:
        smallest=num
    except:
       print("Invalid Input")
       continue
print("Maximum is", largest)
print("Minimum is", smallest)