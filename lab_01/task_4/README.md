# **TASK 04**

## <ins>Cerinta</ins>
>Deoarece tocmai ce ati invatat conceptul de `list comprehension`, acest task va propune urmatoarea cerinta, in care trebuie sa creati o lista cu numele `nice_list`, prin intermediul unei singure linii de cod (`one-liner`, despre care vom vorbi la cursurile viitoare).

>Aceasta lista trebuie sa contina elemente sub forma unor tupluri, astfel:
```
(numar, numar ^ 2, numar ^ 3)
```

>Ulterior, aceste numere trebuie sa respecte urmatoarele conditii:
* numar < 100
* numarul trebuie sa apartina listei `given_numbers`, date ca parametru
* numarul trebuie sa fie ori divizibil cu 2, ori cu 3

## <ins>Input</ins>
>Se da lista cu numere intregi, pozitive , `given_numbers`.

## <ins>Output</ins>
>Salvati lista creata intr-o lista cu numele `nice_list`, lista care, ulterior, va fi returnata.

## <ins>Exemplu</ins>
```
input:
[1, 2, 3, 6, 8, 9, 10, 11, 13, 15, 16, 18, 50, 70, 100, 102, 203]

output:
[(2, 4, 8), (3, 9, 27), (6, 36, 216), (8, 64, 512), (9, 81, 729), (10, 100, 1000), (15, 225, 3375), (16, 256, 4096), (18, 324, 5832), (50, 2500, 125000), (70, 4900, 343000)]
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