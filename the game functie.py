

def punten_telling(superhelden):
    CapsSuperhelden=superhelden
    superhelden = superhelden.lower()
    punten = 25
    GeenPuntenKeerEen=0
    while True:
        guess = input('Raad de character: ')
        guess=guess.lower()
        if superhelden == guess:
            print('Je hebt goed geraden! je hebt nog {} punten over!\nBedankt voor het spelen :D!'.format(str(punten)))
            return Win
        if guess != superhelden:
            print('Je hebt het fout\nProbeer het opnieuw!')
            punten -= 1
            print("Je hebt: {} punten".format(str(punten)))
            if punten>0:
                if punten>3:
                    while True:
                        hint = input('Wil je een hint? ja/nee (kost 3 punten)?: ')
                        if hint.lower()=='ja':
                            print("hier heb je je hint hoer")
                            punten -= 3
                            print(punten)
                            break
                        else:
                            break
                elif GeenPuntenKeerEen<1:
                    print("Je hebt niet genoeg punten om een hint aan te vragen.")
                    GeenPuntenKeerEen=1
            else:
                print("Helaas heb je verloren omdat je geen punten meer over hebt.\nBedankt voor het spelen.")
                print("Het character was {}.".format(CapsSuperhelden))
                return Lose

punten_telling(superhelden)
