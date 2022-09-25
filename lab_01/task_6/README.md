# **TASK 06**

## <ins>Cerinta</ins>
>Pentru acest task, aveti de realizat un cod care sa "deseneze", practic, un romb.

>Marginile rombului vor fi alcatuite din caracterul `@`, pe
cand interiorul va fi reprezentat prin '`.`' (punct).

>Se da parametrul size, care semnifica numarul de linii al rombului. De precizat faptul ca pentru orice size = 2n si size = 2n + 1, romburile rezultate arata la fel, pentru a pastra simetria intacta. Astfel, rombul pentru size = 4 arata la fel cu cel pentru size = 5 s.a.m.d..

>Rombul trebuie creat in interiorul string-ului "romb", unde fiecare linie poate fi despartita prin intermediul caracterului '`\n`'.


## <ins>Observatii</ins>
>Randul cel mai lung (mijlocul rombului) este lipit de marginea din stanga, adica nu exista spatii goale pana la prima margine intalnita.
* size >= 1

## <ins>Exemplu #1</ins>
```
input:
n = 6 || n = 7

output:
   @@
  @..@
 @....@
@......@
 @....@
  @..@
   @@
```

## <ins>Exemplu #2</ins>
```
input:
n = 10 || n = 11

output:
     @@
    @..@
   @....@
  @......@
 @........@
@..........@
 @........@
  @......@
   @....@
    @..@
     @@
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