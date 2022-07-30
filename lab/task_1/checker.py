import os
from task01 import func

# Task 01
print('****************  TASK 01 STARTED  *********************')

all_files = []
for index in range(1, 6):
    file_name = "input/test_" + str(index) + ".txt"
    all_files.append(file_name)

index = 1
for file in all_files:

    lines = []
    with open(file) as f:
        lines = f.readlines()

    note_string = lines[0].split(" ")
    note = [int(element) for element in note_string]
    nume_materie = lines[1]

    pereche = func(note, nume_materie)
    pereche_remastered = ("{:.2f}".format(pereche[0]), pereche[1])
        
    write_file = "output/out_" + str(index) + ".txt"
    g = open(write_file, "w")
    g.write(str(pereche_remastered))
    g.close()

    index += 1

for test_case in range(1, 6):
    out_file = "output/out_" + str(test_case) + ".txt"
    ref_file = "ref/ref_" + str(test_case) + ".txt"

    out_content = open(out_file).readlines()
    ref_content = open(ref_file).readlines()

    if out_content == ref_content:
        print("TEST " + str(test_case) + ".............................. PASSED")
    else:
        print("TEST " + str(test_case) + ".............................. FAILED")

print('**************** TASK 01 COMPLETED *********************')