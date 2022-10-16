# *Online Shopping*

## <ins>Cerinta</ins>

> Deoarece se stie faptul ca matematica este materia preferata a studentilor, acest task va propune sa implementati un sistem de calcul cu numere complexe.

> Astfel, pentru a aprofunda programarea orientata pe obiecte, se doreste implementarea urmatoarelor metode, in interiorul clasei Complex():

>Cu ocazia zilei de Black Friday, un magazin online de electrocasnice nou înființat a pregătit reduceri imbatabile și are nevoie de ajutor pentru partea logistică a site-ului. Fiind la început, magazinul are un stoc alcătuit doar din două tipuri de produse: telefoane și frigidere. Sarcina voastră este să implementati funcționalitățile necesare pentru a fi siguri că site-ul va funcționa cum trebuie.

>Spre exemplu, magazinul va avea următoarele funcționalități:

>User side:

* Odată ce un utilizator se loghează, acesta primește un customer_id unic și poate să își înceapă cumpărăturile(login(self, customer_id));
* Poate adaugă un produs în cart-ul lui (coșul lui de cumpărături) atâta timp cât acesta se află în stoc. Un produs adăugat în cart va dispărea din stoc ( add_to_cart(self, customer_id, product_name));
* Există și situația în care cumpărătorul se poate răzgândi, nu își mai dorește un produs deja adăugat în cart. După ce un produs a fost eliminat din cart, revine iar în stoc (remove_from_cart(self, customer_id, product_name));
* Utilizatorul poate vedea produsele adăugate în cart și prețul acestora, iar dacă încă nu este înregistrat, returnați o lista goală (view_cart(self, customer_id)) La final, plătește produsele, adică returnați suma totală a prețurilor din cart-ul utilizatorului, iar dacă utilizatorul nu este înregistrat se va returna valoarea 0 (checkout(self, customer_id))
Admin side: Implementati metodă pentru că administratorul site-ului să adauge produse în stoc, metodă cu dublu rol, folosită și atunci când utilizatorul a eliminat din cart-ul lui un produs (add(self, new_product))

>De menționat este că magazinul nu va funcționa fără entitățile din spatele acestuia (cartul, produsele, stocul etc.). Completați metodele necesare (TODO) pentru a va asigura că magazinul va funcționa la nivelul așteptărilor clienților.

## <ins>Clasa Product</ins>
```
TODO 1:
    * completeaza constructorul clasei Product

TODO 2:
    * completeaza supraincarcarea operatorului "+"
    * va returna suma preturilor celor doua produse
```
## <ins>Clasa Phone</ins>
```
TODO:
    * supraincarca metoda str
```
## <ins>Clasa Refrigerator</ins>
```
TODO:
    * supraincarca metoda str
```
## <ins>Clasa Stock</ins>
```
TODO 1:
    * adauga un produs nou in stoc

TODO 2:
    * sterge din stocul magazinului produsul dat ca parametru

TODO 3:
    * returneaza stocul curent
```
## <ins>Clasa Cart</ins>
```
TODO 1:
    * adauga un produs in lista de cumparaturi list_cart

TODO 2:
    * sterge produsul din lista de cumparaturi list_card

TODO 3:
    * calculeaza suma preturilor tuturor produselor din cart
    * goleste cartul (in urma cart_checkout, cartul va fi gol)
```
## <ins>Clasa Store</ins>
```
TODO 1:
    * adauga un produs in cart-ul unui cumparator cu id-ul dat
       ** daca cumparatorul nu este logat (id-ul lui nu se gaseste in lista), operatia nu se va realiza (cart-ul ramane neschimbat)
    * odata ce un produs a fost adaugat in cart, este sters din stoc

TODO 2:
    * sterge un produs din cart-ul cumparatorului
        ** daca cumparatorul nu este logat (id-ul lui nu se gaseste in lista), operatia nu se va realiza (cart-ul ramane neschimbat)
    * produsul va fi adaugat iar in stocul magazinului

TODO 3:
    * returneaza lista produselor(nume si pret) din cart

TODO 4:
    * returneaza pretul produselor din cart
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