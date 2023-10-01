import datetime



def calculeaza_X1(an_fabricatie):
    an_curent = datetime.datetime.now().year
    varsta_aparat = an_curent - an_fabricatie
    if varsta_aparat < 7:
        X1 = 0
    else:
        X1 = 1
    return X1


def calculeaza_X2(pret_achizitie, media_cheltuielilor):
    if media_cheltuielilor < 0.1 * pret_achizitie:
        X2 = 0
    elif media_cheltuielilor < 0.2 * pret_achizitie:
        X2 = 1
    elif media_cheltuielilor < 0.3 * pret_achizitie:
        X2 = 2
    else:
        X2 = 3
    return X2


def calculeaza_X3(timp_indisponibilitate, timp_mediu_indisponibilitate):
    if timp_indisponibilitate < 1.5 * timp_mediu_indisponibilitate:
        return 0
    else:
        return 1


def calculeaza_X4(scop_utilizare):
    if scop_utilizare == "mentinerea in viata a pacientului":
        X4 = 4
    elif scop_utilizare == "sprijin terapie":
        X4 = 3
    elif scop_utilizare == "diagnostic":
        X4 = 2
    elif scop_utilizare == "laborator":
        X4 = 1
    else:
        print("Scopul utilizarii nu este valid")
    return X4


def calculeaza_X5(sprijin_producator, serviciu_mentenanta, asigurare_consumabile):
    if sprijin_producator == "Nu" or serviciu_mentenanta == "Nu" or asigurare_consumabile == "Nu":
        X5 = 1
    else:
        X5 = 0
    return X5


def calculeaza_CIP1(X1, X2, X3, X4, X5):
    if X1 not in [0, 1]:
        print("Valoare invalidă pentru X1")

    if X2 not in [0, 1, 2, 3]:
        print("Valoare invalidă pentru X2")

    if X3 not in [0, 1]:
        print("Valoare invalidă pentru X3")

    if X4 not in [1, 2, 3, 4]:
        print("Valoare invalidă pentru X4")

    if X5 not in [0, 1]:
        print("Valoare invalidă pentru X5")

    CIP1 = 9 * (X1 + X2 + X3) + 7.5 * X4 + 25 * X5

    if not(7.5 <= CIP1 <= 100):
        print("Aparatul nu îndeplinește condițiile, trebuie schimbat ")

    return CIP1
