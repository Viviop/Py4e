def Palindrome():
    num=int(input("Enter Number "))
    temp=num
    sum=0
    while(num>0):
        d=num%10
        sum=sum*10+d
        num=num//10
    if(sum==temp):
        print(temp, "is a Palindrome Number")
    else:
        print(temp," is not a Palindrome Number")
Palindrome()