import time
import hashlib
import requests
import json
import random




def charIDtest():
	"string argument"
	loops = 0
	while True:
		loops += 1
		print(loops)
		charID = random.randint(1009146, 1015035)
		print(charID)

		timestamp = str(time.time())
		private_key = "c00f2975204127a291d19b4fc3d5b4978f18356f"  # niet veranderen
		public_key = "ff2fe2f01fbfdc7d228605f74e3ad9fa"  # niet veranderen

		hash = hashlib.md5((timestamp + private_key + public_key).encode('utf-8'))
		md5digest = str(hash.hexdigest())

		url = "https://gateway.marvel.com:443/v1/public/characters/{}".format(charID)
		connection_url = url + "?ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest
		print(connection_url)

		response = requests.get(connection_url)
		jsontext = json.loads(response.text)

		# om de JSON leesbaar te printen...
		# print(json.dumps(jsontext, sort_keys=True, indent=4))

		try:
			print(jsontext['data']['results'][0]['description'])
			print(jsontext['data']['results'][0]['name'])

			if jsontext['data']['results'][0]['description'] == "":
				continue
			else:
				break
		except KeyError:
			continue
	return jsontext


informatie = (charIDtest())

print(informatie['data']['results'][0]['name'])




# print("\nGevonden characters in series:")
# # JSON-indeling kun je uit het geprinte resultaat halen of uit de Marvel docs!
# for item in jsontext['data']['results'][0]['series']['items']:
# 	print(item['name'])

