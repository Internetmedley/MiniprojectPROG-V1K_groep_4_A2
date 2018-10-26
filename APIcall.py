import time
import hashlib
import requests
import json
import random


def ID_test():
    "geen arugment!!!"
    loops = 0

    while True:
        loops += 1
        print(loops)
        infile = open('nonexistentcharIDs.txt', 'r+')
        lines = infile.readlines()
        infile.close()

        charID = random.randint(1009146, 1015035)
        if str(charID) + '\n' in lines or str(charID) in lines:
            continue
        # print(charID)

        timestamp = str(time.time())
        private_key = "c00f2975204127a291d19b4fc3d5b4978f18356f"  # niet veranderen
        public_key = "ff2fe2f01fbfdc7d228605f74e3ad9fa"  # niet veranderen

        hash = hashlib.md5((timestamp + private_key + public_key).encode('utf-8'))
        md5digest = str(hash.hexdigest())

        url = "https://gateway.marvel.com:443/v1/public/characters/{}".format(charID)
        connection_url = url + "?ts=" + timestamp + "&apikey=" + public_key + "&hash=" + md5digest
        # print(connection_url)

        response = requests.get(connection_url)
        jsontext = json.loads(response.text)

        # om de JSON leesbaar te printen...
        # print(json.dumps(jsontext, sort_keys=True, indent=4))

        try:
            jsontext['data']['results'][0]['description']

            if jsontext['data']['results'][0]['description'] == "":
                infile = open('nonexistentcharIDs.txt', 'a')
                infile.write(str(charID) + '\n')
                infile.close()
                continue
            else:
                break
        except KeyError:
            infile = open('nonexistentcharIDs.txt', 'a')
            infile.write(str(charID) + '\n')
            infile.close()
            continue

    with open('informatie.json', 'w') as f:
        json.dump(jsontext, f)
    return


def hero_name():
    "variabele informatie als argument"
    with open('informatie.json', 'r') as f:
        info = json.load(f)
        naam = info['data']['results'][0]['name']
        if '(' in naam:
            return naam.replace(naam[naam.index('(') - 1:], '')
        else:
            return naam


def hero_letters():
    "returnt de hint hoeveel letters de naam bevat"
    with open('informatie.json', 'r') as f:
        info = json.load(f)
        naam = info['data']['results'][0]['name']
        if '(' in naam:
            naam = naam.replace(naam[naam.index('(') - 1:], '')
            hint = 'De naam bevat {} letters.'.format(len(naam))
            return hint
        else:
            hint = 'De naam bevat {} letters.'.format(len(naam))
            return hint


def hero_description():
    "variabele informatie als argument en haalt naam uit de description"
    with open('informatie.json', 'r') as f:
        info = json.load(f)
        naam = info['data']['results'][0]['name']
        if '(' in naam:
            naam = naam.replace(naam[naam.index('(') - 1:], '')
        hint = info['data']['results'][0]['description'].replace(naam, '*****')
        return hint


def eerste_letter():
    ":returns de eerste letter van naam"
    with open('informatie.json', 'r') as f:
        info = json.load(f)
        naam = info['data']['results'][0]['name']
        return naam[0]


def hero_comics():
    ":returns de eerste letter van naam"

    comics = ''
    with open('informatie.json', 'r') as f:
        info = json.load(f)
        for item in info['data']['results'][0]['comics']['items']:
            comics += "{} : ".format(item['name'])
        return comics


def hero_image_URL():
    with open('informatie.json', 'r') as f:
        info = json.load(f)
        imgURL = info['data']['results'][0]['thumbnail']['path'] + '/detail.' + info['data']['results'][0]['thumbnail'][
            'extension']
        return imgURL

# informatie = ID_test()
# print(hero_description(informatie))
# print(hero_letters(informatie))
# print(eerste_letter(informatie))


# print(json.dumps(informatie, sort_keys=True, indent=4))
