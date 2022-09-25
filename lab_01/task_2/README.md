# **TASK 02**

## <ins>Cerinta</ins>
>Ana este eleva in clasa a 9-a la un profil de matematica-informatica. In prima zi de liceu, Doamna Diriginta ii cere Anei sa formeze un tabel cu numele de familie si prenumele colegilor ei.

>Pentru a-si usura munca, Ana te roaga sa o ajuti cu un program in care sa separi numele de familie de prenume.

>Se da, astfel, ca input, o lista de stringuri, fiecare string reprezentand numele complet al unui elev. Trebuie sa separi fiecare nume astfel:

## <ins>Input</ins>
>Se da lista de stringuri `nume_complete`.

## <ins>Output</ins>
>Trebuie sa creezi un tuplu `nume_formatat`, care sa contina, ca prim element, o lista cu toate numele de familie, ca al doilea element, o lista cu primele prenume si apoi o lista cu celelalte prenume.

## <ins>Observatie</ins>
>Toate numele sunt de forma: 
>{`Nume_familie`} {`Prenume #1`}-{`Prenume #2`}.

## <ins>Exemplu</ins>
 
```
input:
Popescu Gabriel-Ion

--->
Nume familie = Popescu
Prenume #1 = Gabriel
Prenume #2 = Ion
```

## <ins>Rulare | Testare</ins>

> Pentru testare, puteți rula script-ul direct din IDE sau puteți rula în terminal comanda:

```
./checker.py
```

> In cazul in care nu puteti rula acest script din cauza permisiunilor, folositi mai intai urmatoarea comanda:

```
sudo chmod 700 checker.py
```