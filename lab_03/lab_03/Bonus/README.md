# **Bonus**

## <ins>Cerinta</ins>

> Deoarece se stie faptul ca matematica este materia preferata a studentilor, acest task va propune sa implementati un sistem de calcul cu numere complexe.

> Astfel, pentru a aprofunda programarea orientata pe obiecte, se doreste implementarea urmatoarelor metode, in interiorul clasei Complex():
    
* ##### def __init__(self, real_part: int, imaginary_part: int, var_name: str = 'var') -> None:
* ##### def __str__(self) -> str:
* ##### def add_complex_numbers(self, other) -> None:
* ##### def substract_complex_numbers(self, other) -> None:
* ##### def multiply_complex_numbers(self, other) -> None:
> Pentru simplitate, schimbarile produse in urma operatiilor efectuate se vor realiza asupra obiectului care apeleaza metodele respective.

> i<sup>2</sup> = -1

> La apelarea metodei \_\_str__, se doreste afisarea cat mai corecta a numarului complex, precum in urmatorul exemplu:

```
Fie z = x + yi

La afisare:
x = 0          ---> z = yi
y = 0          ---> z = x
x = 0 && y = 0 ---> z = 0
y < 0          ---> z = x - yi
               ---> nu se accepta: z = 1 - -2i
```
## <ins>Exemplu</ins>
```
a = Complex(1, 2, 'a')
>> "Complex number succesfully created."
b = Complex(0, 2, 'b')
>> "Complex number succesfully created."
print(a)
>> a = 1 + 2i
print(b)
>> b = 2i
a.multiply_complex_numbers(b)
print(a)
>> a = -4 + 2i
print(b)
>> b = 2i
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