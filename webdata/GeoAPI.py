import urllib.request
import urllib.parse
import json

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

address = input('Enter location: ')

# Encode address into URL parameters
params = {'q': address}
url = serviceurl + urllib.parse.urlencode(params)

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

# Load JSON
js = json.loads(data)

# Get the plus_code from the first feature
plus_code = js['features'][0]['properties']['plus_code']
print('Plus code', plus_code)