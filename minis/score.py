try:
 score = float(input("Enter Score: "))
except:
 print("Enter Numeric Value")
 quit()
if(1>=score>=0.9):
 print("A")
elif(0.9>score>=0.8):
 print("B")
elif(0.8>score>=0.7):
 print("C")
elif(0.7>score>=0.6):
 print("D")
elif(0<score<0.6):
 print("F")
else:
  print("Enter Valid Score between 0 and 1")