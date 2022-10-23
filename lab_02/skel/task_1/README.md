# **TASK 01**

## <ins>Cerinta</ins>

> Gigel a inceput noul curs de paradigme de programare, insa nu a inteles foarte bine functionalele **map** si **filter**. De aceea, el va avea nevoie sa il ajutati cu 3 task-uri:
* sa dubleze toate numerele care se divid cu 6, iar pe cele care nu, sa le tripleze;
* sa transforme in litere mari toate vocalele dintr-o fraza (nu e nevoie sa luati in considerare diacriticele)
* sa selecteze dintr-o lista doar cuvintele palindrom (se garanteaza ca toate cuvintele contin doar litere mici)

## <ins>Exemplu</ins>

```
Task 1a
input:
24 3 8 18 9 6 27

output:
48 9 24 36 27 12 81
```

```
Task 1b
input:
Gigel a inceput sa invete

output:
GIgEl A IncEpUt sA InvEtE
```

```
Task 1c
input:
demigod madam python php

output:
madam php
```

> Indicatii de rezolvare:
* folositi-va de functii lambda (cu if else sau fara) sau construiti-va functii aditionale
* pentru instructiuni if else in expresii lambda puteti consulta site-ul: https://thispointer.com/python-how-to-use-if-else-elif-in-lambda-functions/
* ajutati-va de un vector/string de vocale pentru Task 1b

> Explicatii pentru valorile de retur din schelet:
* dupa ce se aplica functionale, noul rezultat va fi de tipul "nume_functionala object" 
* folosim list pentru a converti rezultatul intors de functionala intr-o lista
* mai multe detalii aici: https://www.pythonmorsels.com/map-and-filter-python/

## <ins>Rulare | Testare</ins>

> Pentru testare, puteți rula script-ul direct din IDE sau puteți rula în terminal comanda:

```
./checker.py
```

> In cazul in care nu puteti rula acest script din cauza permisiunilor, folositi mai intai urmatoarea comanda:

```
sudo chmod 644 checker.py
```