from PROG import APIcall
from PROG import scoredisplay


# informatie = APIcall.ID_test()
# superhelden = APIcall.hero_name(informatie)


def punten_telling():
    while True:
        informatie = APIcall.ID_test()
        superhelden = APIcall.hero_name(informatie)

        CapsSuperhelden = superhelden
        superhelden = superhelden.lower()
        punten = 25
        GeenPuntenKeerEen = 0
        scoredisplay.high_score_print()
        while True:
            guess = input('Raad de superhelden: ')
            guess = guess.lower()
            if superhelden == guess:
                print('Je hebt goed geraden! je hebt nog {} punten over!\nBedankt voor het spelen :D!'.format(
                    str(punten)))
                break
            if guess != superhelden:
                print('Je hebt het fout\nProbeer het opnieuw!')
                punten -= 1
                print("Je hebt: {} punten".format(str(punten)))
                if punten > 0:
                    if punten > 3:
                        while True:
                            hint = input('Wil je een hint? ja/nee (kost 3 punten)?: ')
                            LowerHint = hint.lower()
                            if LowerHint == ('ja'):
                                punten -= 3
                                print("Je hebt: {} punten".format(str(punten)))
                                print('hint!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1')
                                break
                            elif LowerHint == ('nee'):
                                break
                            else:
                                print('voer ja of nee in!')
                    elif GeenPuntenKeerEen < 1:
                        print("Je hebt niet genoeg punten om een hint aan te vragen.")
                        GeenPuntenKeerEen = 1
                else:
                    print("Helaas heb je verloren omdat je geen punten meer over hebt.\nBedankt voor het spelen.")
                    print("De superheld was {}.".format(CapsSuperhelden))
                    break
        scoredisplay.high_score_check(punten)
        scoredisplay.high_score_print()

punten_telling()
