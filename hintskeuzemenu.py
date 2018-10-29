import APIcall
informatie = APIcall.ID_test()

hintKeuzeDict = {'1' : APIcall.hero_description(),
                 '2' : APIcall.hero_letters(),
                 '3' : APIcall.eerste_letter(),
                 '4' : APIcall.hero_comics()}

hintDisplayDict = {'1': "een beschrijving van het te raden character.",
                   '2': "het aantal letters van het te raden character.",
                   '3': "de eerste letter van het te raden character.",
                   '4': "een aantal comics waar het te raden character in voorkomt."}

def hint_keuzemenu(dict):
    for key, value in dict.items():
        print("{} : {}".format(key, value))


def hint_keuzeinvoer(dict):

    while True:
        keuze = input("Keuze: ")
        try:
            print(dict.pop(keuze))
            hintDisplayDict.pop(keuze)
            break
        except KeyError:
            print("Dit is geen geldige invoer, probeer het nog eens.")
            continue


# hint_keuzemenu(hintDisplayDict)
hint_keuzeinvoer(hintKeuzeDict)
# print(hintKeuzeDict)
# hint_keuzemenu(hintDisplayDict)
hint_keuzeinvoer(hintKeuzeDict)
