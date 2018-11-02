import json
from datetime import date


def high_score_print():
    """print de geformatteerde string van de high-scorelijst met keys en values gehaald uit 'hi-scores.json'."""
    with open('hi-scores.json', 'r') as f:
        data = json.load(f)

    hiscore = ''
    for key, value in data.items():
        hiscore += ("{:14}\t\t{:2}\n".format(key, value))
    return hiscore


def daily_high_scores_print():
    """print de geformatteerde string van de daily high-scorelijst gehaald uit 'daily-hi-score.json'.
    de key die hiervoor wordt gebruikt is de datum van vandaag, als de datum van vandaag niet de goede key is
    omdat het een daily high-score van gisteren betreft bijvoorbeeld, zal hij een keyError geven die opgevangen wordt.
    Dan wordt er i.p.v. de geformatteerde string met de keys en values dus een andere string gereturnt."""
    vandaag = str(date.today())
    with open('daily-hi-score.json', 'r') as f:
        dailyDict = json.load(f)
    try:
        dailyhiscore = ''
        for key, value in dailyDict[vandaag].items():
            dailyhiscore += ("{:14}\t\t{:2}\n".format(key, value))
    except KeyError:
        dailyhiscore += "No entries in the daily hi-score!\n" \
                   "Play now to earn a spot!"
    return dailyhiscore


# def high_score_check(score, username):
#     "deze code wordt niet gebruikt in de final version."
#     with open('hi-scores.json', 'r') as f:
#         data = json.load(f)
#
#     if score > min(data.values()):                                              # checkt score hoog genoeg is
#         while True:
#             if len(username) > 14:
#                 print("Uw gebruikersnaam is te lang. Probeer het nog eens.")
#                 continue
#             elif len(username) < 2:
#                 print("Uw gebruikersnaam is te kort. Probeer het nog eens.")
#                 continue
#             elif username in data.keys():                        # anders fuckt het met de dictionary en values
#                 print("Uw gebruikersnaam is al in gebruik. Kies een andere.")
#                 continue
#             else:                                    # als alle systemen nominaal zijn(goed dus)
#                 data.update({username: score})
#                 break
#     else:
#         print("Uw score is niet hoog genoeg om in de rankings te komen.")
#
#     lijstKeys = (sorted(data, key=data.__getitem__, reverse=True))              # maakt lijst van keys van reverse gesorteerde values
#     lijstValues = (sorted(data.values(), reverse=True))                         # maakt lijst van reverse gesorteerde values
#
#     data.clear()
#     for i in range(0, 10):
#         try:
#             data.update({lijstKeys[i]: lijstValues[i]})
#         except:
#             break
#
#     with open('hi-scores.json', 'w') as f:
#             json.dump(data, f)
#     return


