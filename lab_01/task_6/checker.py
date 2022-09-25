#!/usr/bin/python3

import os
from task06 import func

# Task 01
print('****************  TASK 06 STARTED  *********************')

all_files = []
for index in range(1, 7):
    file_name = "tests/in/test_" + str(index) + ".in"
    all_files.append(file_name)

index = 1
for file in all_files:

    lines = []
    with open(file) as f:
        lines = f.readlines()

    size = lines[0]
    romb = func(int(size))

    write_file = "tests/out/test_" + str(index) + ".out"
    g = open(write_file, "w")
    g.write(romb)
    g.close()

    index += 1

for test_case in range(1, 7):
    out_file = "tests/out/test_" + str(test_case) + ".out"
    ref_file = "tests/ref/test_" + str(test_case) + ".ref"

    out_content = open(out_file).readlines()
    ref_content = open(ref_file).readlines()

    if out_content == ref_content:
        print("TEST " + str(test_case) + ".............................. PASSED")
    else:
        print("TEST " + str(test_case) + ".............................. FAILED")

print('**************** TASK 06 COMPLETED *********************')
