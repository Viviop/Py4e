def ArmStrong():
  num=int(input("Enter Number "))
  temp=num
  sum=0
  while(num>0):
    d=int(num%10)
    sum=sum+d**3
    num=int(num/10)
  if(sum==temp):
    print(temp, "is an Armstrong number")
  else:
    print(temp, "is not an Armstrong number")
  
ArmStrong()