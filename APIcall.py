import time
import hashlib
import requests
import json
import random


def ID_test():
    """gaat zoeken naar een geschikte character ID door een random int te pakken tussen de ID's 1009146 en 1015035
    en die op te vragen met requests, en als de json die gereturnt wordt
    geen key 'description' heeft (of description is een lege string ''), dan loopt hij nog een keer totdat
    hij er wel een gevonden heeft en dan stopt hij de json text in 'informatie.json'.
    De 'slechte' character ID's - waar dus geen description in zit - zet hij in de text file 'nonexistentcharIDs.txt'
    zodat hij die ID's onthoudt en skipt als hij die weer tegen komt zodat het programma sneller loopt en hij minder
    onnodige API requests hoeft te versturen naar Marvel naar verloop van tijd."""
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

            if jsontext['data']['results'][0]['description'] == "" or jsontext['data']['results'][0]['description'] == " ":
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
    """pakt de naam van de character uit 'informatie.json' en als er een '(' in zit haalt hij
    alles wat tussen de haakjes zit weg mét de spatie die voor het eerste haakje staat.
    Dan returnt hij de naam als string."""
    with open('informatie.json', 'r') as f:
        info = json.load(f)
        naam = info['data']['results'][0]['name']
        if '(' in naam:
            return naam.replace(naam[naam.index('(') - 1:], '')
        else:
            return naam


def hero_letters():
    """returnt het aantal letters van de naam die uit hero_name() komt."""
    naam = hero_name()
    lengte = 'The name contains {} letters.'.format(len(naam))
    return lengte


def hero_description():
    """haalt de character naam uit hero_name() en filter de description gehaalt uit de API
    zodat de naam niet in de description zal zitten (anders zou deze hint overpowered zijn)."""
    with open('informatie.json', 'r') as f:
        info = json.load(f)
        naam = hero_name()
        description = info['data']['results'][0]['description'].replace(naam, '*****')
        return description


def eerste_letter():
    """returnt de eerste letter van de character naam."""
    with open('informatie.json', 'r') as f:
        info = json.load(f)
        naamEersteLetter = "The first letter is a '{}'.".format(info['data']['results'][0]['name'][0])
        return naamEersteLetter


def hero_comics():
    """"returnt de eerste letter van de character naam en stopt die in de string 'comics'."""
    comics = ''
    with open('informatie.json', 'r') as f:
        info = json.load(f)
        for item in info['data']['results'][0]['comics']['items']:
            comics += "{} : ".format(item['name'])
        return comics


def hero_image_url():
    """returnt de URL van het .jpg bestand uit informatie.json """
    with open('informatie.json', 'r') as f:
        info = json.load(f)
        imgurl = info['data']['results'][0]['thumbnail']['path'] + '/portrait_uncanny.' + \
                 info['data']['results'][0]['thumbnail']['extension']
        return imgurl
