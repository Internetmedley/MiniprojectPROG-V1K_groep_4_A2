import json


def high_score_check(score):
    "checkt of de high-score hoog genoeg is en dan voegt ie hem toe"
    with open('hi-scores.json', 'r') as f:
        data = json.load(f)

    if score > min(data.values()):                                              #checkt score hoog genoeg is
        while True:
            userName = input("Kies een gebruikersnaam(min. 2, max 14): ")
            if len(userName) > 14:
                print("Uw gebruikersnaam is te lang. Probeer het nog eens.")
                continue
            elif len(userName) < 2:
                print("Uw gebruikersnaam is te kort. Probeer het nog eens.")
                continue
            elif userName in data.keys():                                       #anders fuckt het met de dictionary en values
                print("Uw gebruikersnaam is al in gebruik. Kies een andere.")
                continue
            else:           #als alle systemen nominaal zijn(goed dus)
                data.update({userName : score})
                break
    else:
        print("Uw score is niet hoog genoeg om in de rankings te komen.")


    lijstKeys = (sorted(data, key=data.__getitem__, reverse=True))              #maakt lijst van keys van reverse gesorteerde values
    lijstValues = (sorted(data.values(), reverse=True))                         #maakt lijst van reverse gesorteerde values

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
    "print de high-scorelijst"
    with open('hi-scores.json', 'r') as f:
        data = json.load(f)

    hiscore = ''
    for key, value in data.items():
        hiscore += ("{:14}\t\t{:2}\n".format(key, value))

    return hiscore


# high_score_check(30)
# high_score_print()
#kan niet zelfde key als eentje die al bestaat
