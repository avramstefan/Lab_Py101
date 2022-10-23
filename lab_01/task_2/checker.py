#!/usr/bin/python3

import os
from task02 import func

# Task 01
print('****************  TASK 02 STARTED  *********************')

path = os.getcwd() + "/tests/out"
try:
    os.mkdir(path)
except OSError:
    print(end = "")

lines = []
with open("tests/in/test.in") as f:
    lines = f.readlines()

pereche = func(lines)

pereche_list = list(pereche)
for i in range(len(pereche_list[2]) - 1):
    pereche_list[2][i] = pereche_list[2][i][:-1]

pereche = tuple(pereche_list)
    
write_file = "tests/out/test.out"
g = open(write_file, "w")
g.write("Nume familie:\n" + str(pereche[0]) + "\n\n" + "Prenume_1:\n" +\
         str(pereche[1]) + "\n\n" + "Prenume_2:\n" + str(pereche[2]))
g.close()

out_file = "tests/out/test.out"
ref_file = "tests/ref/test.ref"

out_content = open(out_file).readlines()
ref_content = open(ref_file).readlines()

if out_content == ref_content:
    print("TASK 02.............................. PASSED")
else:
    print("TASK 02.............................. FAILED")

print('**************** TASK 02 COMPLETED *********************')