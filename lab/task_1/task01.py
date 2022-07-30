def func(note, nume_materie):

    # Trebuie sa creati un tuplu cu numele "pereche",
    # in care veti tine, astfel, (media notelor, numele_materiei)

    medie = 0
    for nota in note:
        medie += nota
    medie /= len(note)
    pereche = (medie, nume_materie) 

    return pereche
