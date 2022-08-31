# MODULE

## Task 01
Se da functia `random_points(radius, center_x, center_y)`, ce primeste raza si centrul cercului, reprezentat prin perechea de coordonate `[x_center, y_center]`. Functia returneaza coordonatele unui punct random din interiorul cercului. 

__Va puteti folosi de modulele math si random.__

_(If you can't remember the math: https://doubleroot.in/lessons/circle/position-of-a-point/)_

### Exemplu
```
input: 1.25 0 3.4
output: [0.48334197442603744, 4.286286596848848]
```

## Task 02
Un fisier PPM (Portable Pix Map) descrie o imagine intr-o forma usor de inteles. 

Fisierul are 2 componente:

- Header
    1. Formatul fisierului _(Vom lucra cu reprezentarea in ASCII, deci vom folosi doar P3 atat pentru citire, cat si pentru scriere)_
    2. Numarul de linii (N), respectiv de coloane (M) din body
    3. Valoarea maxima pentru culori _(Vom folosi 255)_
- Body
    1. O "matrice" de N linii si M coloane de triplete cu valori de tip intreg, ce reprezinta valorile pixelilor in canalul RGB. _(Adica fiecare pixel va fi reprezentat prin 3 valori: R, G si B. De exemplu, un pixel reprezentat prin [255 0 0] va fi de culoare rosie)_. 

Exemplu:
```python
P3 #file format
3 3 # N x M
255 #maximum color value
#the P3 means colors are in ascii, then 3 columns and 3 rows, then 255 for max color, then RGB triplets 
255 0 0 0 255 0 0 0 255 
255 255 0 255 255 255 0 0 0 
0 255 255 75 75 75 127 127 127
#the first pixel [255 0 0] means RED = 255, GREEN = 0, BLUE = 0. So the pixel is red. 
```
__Fisierele de intrare nu vor contine comentarii, pentru a usura citirea.__
### Task 02.1
Completati functia read din task02.py.

***HINT: Observati functiile vstack si hstack din modulul numpy explicate aici:*** https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html

### Task 02.2
Folosind informatiile extrase din imagine la punctul anterior, completati functia sepia, folosind formulele:
```python
sepia_r = (int)(0.393*r + 0.769*g + 0.189*b)
sepia_g = (int)(0.349*r + 0.686*g + 0.168*b)
sepia_b = (int)(0.272*r + 0.534*g + 0.131*b)
#r, g si b reprezinta canelele
# nu uitati de cazul in care aplicand formula se poate depasi valoarea maxima a culorii
```
Pentru exemplul dat mai sus, rezulta imaginea:
```python
P3
3 3
255
100 88 69 196 174 136 48 42 33
296 263 205 344 306 238 0 0 0
244 217 169 101 90 70 171 152 118
```


## Rulare checker
```python
./checker.py numar_task numar_subtask
```
Argumentele sunt optionale. Pentru un task cu mai multe subtask-uri se poate verifica complet sau fragmentat:
```python
./checker.py 2
#task 3 complet
./checker.py 2 1
#task 2 subtask 1
# ``` 
