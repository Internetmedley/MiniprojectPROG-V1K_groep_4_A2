import json

# invoerNaam =  input("Name: ")
# score = 20

def high_score_check(score):
    "checkt of de high-score hoog genoeg is en dan voegt ie hem toe"
    with open('hi-scores.json', 'r') as f:
        data = json.load(f)

    if score > min(data.values()):
        while True:
            userName = input("Kies een gebruikersnaam(max. 14 characters): ")
            if len(userName) > 14:
                print("Uw gebruikersnaam is te lang. Probeer het nog eens.")
                continue
            elif userName in data.keys():
                print("Uw gebruikersnaam is al in gebruik. Kies een andere.")
                continue
            else:
                data.update({userName : score})
                break
    else:
        print("Uw score is niet hoog genoeg om in de rankings te komen.")


    lijstKeys = (sorted(data, key=data.__getitem__, reverse=True))
    lijstValues = (sorted(data.values(), reverse=True))

    data.clear()
    for i in range(0, 10):
        try:
            data.update({lijstKeys[i]: lijstValues[i]})
        except:
            break

    with open('hi-scores.json', 'w') as f:
            json.dump(data, f)
    return


def high_score_print():
    with open('hi-scores.json', 'r') as f:
        data = json.load(f)

    hiscore = ''
    for key, value in data.items():
        hiscore += ("{:14}\t\t{:2}\n".format(key, value))

    return print(hiscore)



high_score_check(22)
high_score_print()
#kan niet zelfde key als eentje die al bestaat