def func(nume_complete):
    """
    Creeaza un tuplu "nume_formatat" care sa contina 3 elemente:
    nume_formatat[0] = lista cu numele de familie
    nume_formatat[1] = lista cu primele prenume
    nume_formatat[2] = lista cu celelalte prenume

    HINT!  conversie string - lista || (string.split("delimiter"))
    """

    ################### TO DO #########################
    
    nume_fam = []
    prenume_1 = []
    prenume_2 = []

    for name in nume_complete:
        nume_lista = name.split(" ")
        nume_fam.append(nume_lista[0])
        prenume = nume_lista[1].split("-")
        prenume_1.append(prenume[0])
        prenume_2.append(prenume[1])

    nume_formatat = (nume_fam, prenume_1, prenume_2)

    ###################################################

    return nume_formatat
    