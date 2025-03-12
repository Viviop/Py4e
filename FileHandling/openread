# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
summation=0.0
count=0.0
fh = open(fname)
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        pos=line.find(':')
        summation=summation+float(line[pos+1:])
        count=count+1.0
avg=summation/count
print("Average spam confidence: ",avg)
