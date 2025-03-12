file=input("File Name: ")
fh=open(file)

for line in fh:
    words=line.split()
    if len(words)<3 or words[0] != 'From':
        continue
    print(words[2])