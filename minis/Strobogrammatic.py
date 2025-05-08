num=int(input("Enter a Number: "))
valid=True
def Strobogrammatic(n):
  rev=0
  valid=True
  while(n>0):
    d=int(n%10)
    if(d==6):
      d=9
    elif(d==9):
      d=6
    elif(d==8 or d==1 or d==0):
      d=d
    else:
       valid=False
    rev=(rev*10)+d
    n=n//10
  return rev,valid

for i in range(10**(num-1), 10**num):
  rev,valid=Strobogrammatic(i)
  if(rev==i  and  valid):
    print(i)