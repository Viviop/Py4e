import urllib.request
import json

url = input('Enter location: ')
if len(url) < 1 : 
    url = 'https://py4e-data.dr-chuck.net/comments_2159779.json'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()

info=json.loads(data)
sum=0
for person in info["comments"]:
    sum=sum+int(person["count"])
print(sum)