# **TASK 03**

## <ins>Cerinta</ins>
>Gigel si fratele sau vor sa comunice fara ca parintii lor sa inteleaga despre ce vorbesc. Astfel, acestia s-au gandit la o metoda de codificare a mesajelor.

>Prima regula este aceea ca fiecare mesaj contine doar majuscule si spatii goale. Ulterior, codificarea va consta in realizarea unui program in care se creeaza un mesaj format din cifre, unde fiecare cifra reprezinta indexul literei respective in alfabet. Pentru spatiu, se va scrie cifra '0'.

## <ins>Input</ins>
>Se da stringul (mesajul care trebuie codificat) `string_message`.

## <ins>Output</ins>
>Salvati mesajul codificat intr-un string `encoded_message`.

## <ins>Explicatie</ins>
    A   B   C   D   E   F   G     H   I
    |   |   |   |   |   |   |  |  |   |
    1   2   3   4   5   6   7  0  8   9                             

    Pentru A -> index alfabet = 1
           B -> index alfabet = 2
           C -> index alfabet = 3
           .............
           Z -> index alfabet = 26
    iar pentru ' ' -> codificare = 0

## <ins>Exemplu</ins>
```
input:
ANA NU ARE MERE

output:
114101421011850135185
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