import time
import hashlib
import requests
import json

spiderManId = "1009610"

timestamp = str(time.time())
private_key = "c00f2975204127a291d19b4fc3d5b4978f18356f"	#niet veranderen
public_key = "ff2fe2f01fbfdc7d228605f74e3ad9fa"			#niet veranderen

hash = hashlib.md5( (timestamp+private_key+public_key).encode('utf-8') )
md5digest = str(hash.hexdigest())

url = "https://gateway.marvel.com:443/v1/public/characters/{}".format(spiderManId)
connection_url = url+"?ts="+timestamp+"&apikey="+public_key+"&hash="+md5digest
print(connection_url)


response = requests.get(connection_url)
jsontext = json.loads(response.text)

# om de JSON leesbaar te printen...
# print(json.dumps(jsontext, sort_keys=True, indent=4))


print("\nGevonden characters in comics:")
# JSON-indeling kun je uit het geprinte resultaat halen of uit de Marvel docs!
for item in jsontext['data']['results']:			#gaat zoeken in data, dan results
	gekozenSuperheld = item['name']					#print name uit data\results, bekijk https://developer.marvel.com/docs#!/public/getCreatorCollection_get_0 voor meer info
	print(item['description'], '\n' + item['name'] + '\n')

print(type(gekozenSuperheld))

# print("\nGevonden characters in series:")
# # JSON-indeling kun je uit het geprinte resultaat halen of uit de Marvel docs!
# for item in jsontext['data']['results'][0]['series']['items']:
# 	print(item['name'])