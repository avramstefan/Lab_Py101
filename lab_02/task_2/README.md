# **TASK 02**

## <ins>Cerinta</ins>

> Astazi ati observat ca functiile in Python pot avea un numar variabil de parametri. Pentru acest task veti primi ca input mai multe argumente dintre care va trebui sa le pastrati doar pe cele care respecta una din conditiile:
* sa fie numere **intregi**
* sa fie consoane mici

## <ins>Exemplu</ins>

```
input:
50 'A' 8.2 'c' '_' 3 'n' True 'Z' [1,2] 't'

output:
50 'c' 3 'n' 't'
```

> Indicatii de rezolvare:
* folositi-va de functia type
* daca folositi functia isinstance, luati in calcul faptul ca variabilele tip bool True/False sunt considerate int-uri 1/0

## <ins>Rulare | Testare</ins>

> Pentru testare, puteți rula script-ul direct din IDE sau puteți rula în terminal comanda:

```
./checker.py
```

> In cazul in care nu puteti rula acest script din cauza permisiunilor, folositi mai intai urmatoarea comanda:

```
sudo chmod 644 checker.py
```