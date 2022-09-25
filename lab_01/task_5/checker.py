#!/usr/bin/python3

import os
from task05 import zig_zag

# Task 01
print('****************  TASK 05 STARTED  *********************')

all_files = []
for index in range(1, 6):
    file_name = "tests/in/test_" + str(index) + ".in"
    all_files.append(file_name)

index = 1
for file in all_files:

    lines = []
    with open(file) as f:
        lines = f.readlines()

    dim = lines[0].split(' ')
    rows = int(dim[0])
    cols = int(dim[1])

    zig_zag_matrix = zig_zag(rows, cols)

    write_file = "tests/out/test_" + str(index) + ".out"
    g = open(write_file, "w")
    for i in range(rows):
        g.write(str(zig_zag_matrix[i]) + "\n")
    g.close()

    index += 1

for test_case in range(1, 6):
    out_file = "tests/out/test_" + str(test_case) + ".out"
    ref_file = "tests/ref/test_" + str(test_case) + ".ref"

    out_content = open(out_file).readlines()
    ref_content = open(ref_file).readlines()

    if out_content == ref_content:
        print("TEST " + str(test_case) + ".............................. PASSED")
    else:
        print("TEST " + str(test_case) + ".............................. FAILED")

print('**************** TASK 05 COMPLETED *********************')
