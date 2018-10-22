import APIcall
informatie = APIcall.ID_test()
print(informatie)
print(APIcall.hero_name(informatie))
print(APIcall.hero_description(informatie))
print(APIcall.hero_letters(informatie))
print(APIcall.hero_comics(informatie))
print(APIcall.eerste_letter(informatie))
APIcall.hero_description(informatie)
APIcall.hero_letters(informatie)
APIcall.hero_comics(informatie)
APIcall.hero_letters(informatie)

nummer_lijst = [1, 2, 3, 4]

def hint_keuze(nummer_lijst):
    keuze1=0
    keuze2=0
    keuze3=0
    keuze4=0
    while True:
        print("U heeft een hint aangevraagd.")
        if keuze1==0:
            print("1. Omschrijving van de character")
        if keuze2==0:
            print("2. Aantal letters")
        if keuze3==0:
            print("3. Comics waar de character in voorkomt")
        if keuze4==0:
            print("4. De eerste letter(s) van zijn/haar naam")
        keuze_menu= input("Wat voor soort hint wilt u krijgen? (vul {} in): ".format(nummer_lijst))
        keuze=keuze_menu.lower()
        while True:
            if keuze=='één' or 'een' or '1' and keuze1==0:
                print("Keuze 1: De omschrijving van de character:")
                print(APIcall.hero_description(informatie))
                keuze1=1
                nummer_lijst.remove(1)
                break
            elif keuze=='twee' or '2' and keuze2==0:
                print("Keuze 2: Aantal letters van de character:")
                print(APIcall.hero_letters(informatie))
                keuze2=1
                nummer_lijst.remove(2)
                break
            elif keuze=='drie' or '3' and keuze3==0:
                print("Keuze 3: Comics waar de character in voorkomt:")
                print(APIcall.hero_comics(informatie))
                keuze3=1
                nummer_lijst.remove(3)
                break
            elif keuze=='vier' or '4' and keuze4==0:
                print("De eerste letter(s) van zijn/haar naam:")
                print(APIcall.hero_letters(informatie))
                keuze4=1
                nummer_lijst.remove(4)
                break
            else:
                input("U moet {} kiezen!: ".format(nummer_lijst))