from MiniprojectPROG import APIcall
superhelden = APIcall.apicallcharID("1009610")
'superhelden naam in lowercase'
# while True:
#     import random
#     ID = print(random.randint(1009146, 1015035))
#     # random.rantint is tot en met
#     if len(superhelden) > 1:
#         continue
#     else:
#         break


def punten_telling():
    punten = 25
    while True:
        guess = str(input('welke superheld?: '))
        guess.lower()
        if guess == superhelden:
            print('je hebt goed geraden! je hebt nog ' + str(punten) + ' punten over')
            return False
        if guess != superhelden:
            print('je hebt het fout')
            punten -= 1
            print('je hebt: ' + str(punten))
            while True:
                hint = input('wil je een hint? j/n (kost 3 punten)')
                if hint == ('j'):
                    punten -= 3
                    print('je hebt nu: ' + str(punten))
                    break
                elif hint == ('n'):
                    break
                else:
                    print('voer j of n in!')

punten_telling()