# **TASK 03**

## <ins>Cerinta</ins>

> Pentru acest task o sa facem un joc de imaginatie: sunteti interni la secretariatul din poli si doriti sa extrageti din catalog numele tuturor studentilor care au media anuala mai mare sau egala cu 8.50 pentru a le acorda burse.

> Catalogul este sub forma unui dictionar, in care cheia este numele studentului, iar valoarea este o lista de note. Calculati media pentru fiecare student si returnati o lista cu numele celor care se incadreaza pentru bursa.

## <ins>Exemplu</ins>

```
input:
{
    "Andrei Sava": [8, 7, 8, 10, 8]
    "Irina Barbu": [9, 7, 10, 10, 9]
    "Matei Popa": [10, 10, 8, 10, 10]
}

output:
['Irina Barbu', 'Matei Popa']
```

> Indicatii de rezolvare:
* folositi-va de functii lambda sau creati-va o functie aditionala pentru a verifica daca un student are media corespunzatoare

## <ins>Rulare | Testare</ins>

> Pentru testare, puteți rula script-ul direct din IDE sau puteți rula în terminal comanda:

```
./checker.py
```

> In cazul in care nu puteti rula acest script din cauza permisiunilor, folositi mai intai urmatoarea comanda:

```
sudo chmod 700 checker.py
```