name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    words=line.split()
    for word in words:
        if word!='From':
            continue
        else:
            time=words[5].split(':')
            counts[time[0]]=counts.get(time[0],0)+1

cool=sorted(counts.items())
for k,v in cool:
    print(k,v)