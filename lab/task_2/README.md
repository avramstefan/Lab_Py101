$$TASK....02$$

Pentru testare, puteți rula în terminal comanda `python3 checker.py` sau puteți rula script-ul direct din IDE.

### **Cerinta**
        Ana este eleva in clasa a 9-a la un profil de matematica-informatica. In prima zi de liceu, Doamna Diriginta ii cere Anei sa formeze un tabel cu numele de familie si prenumele colegilor ei.

        Pentru a-si usura munca, Ana te roaga sa o ajuti cu un program in care sa separi numele de familie de prenume.

        Se da, astfel, ca input, o lista de stringuri, fiecare string reprezentand numele complet al unui elev. Trebuie sa separi fiecare nume astfel:

## Exemplu
                             Popescu Ion Gigel
                                    |
                                    |
                        Nume     Prenume_1    Prenume_2

                        Popescu     Ion          Gigel

        Fiecare string va avea formatul:
        **{Nume familie} {Prenume_1} {Prenume_2}**

## Output
    Trebuie sa creezi un tuplu "nume_formatat", care sa contina, ca prim element, o lista cu toate numele de familie, ca al doilea element, o lista cu primele prenume si apoi o lista cu celelalte prenume.