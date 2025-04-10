#find highest freq of who sent mail
name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        if word != 'From':
            continue
        else:
            counts[words[1]]=counts.get(words[1],0) + 1

maxc=0 
maxw=None
for key,value in counts.items():
    if maxc==0 or maxc<value:
        maxw=key
        maxc=value

print(maxw,maxc)