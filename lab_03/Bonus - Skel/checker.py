#!/usr/bin/python3

import os
import sys
import task01 as c

# Task 01
print('****************  TASK 01 STARTED  *********************')

path = os.getcwd() + "/tests/out"
try:
    os.mkdir(path)
except OSError:
    print(end = "")

all_files = []
for index in range(1, 6):
    file_name = "tests/in/test_" + str(index) + ".in"
    all_files.append(file_name)

index = 1
original_stdout = sys.stdout
for file in all_files:

    sys.stdout = open("tests/out/tmp_" + str(index) + ".out", 'w')

    content = ""
    with open(file) as f:
        content = f.read()

    exec(content)
    sys.stdout = original_stdout

    input_content = []
    tmp_content = []

    with open(file) as f:
        input_content = f.readlines()
    
    with open("tests/out/tmp_" + str(index) + ".out") as f:
        tmp_content = f.readlines()
    
    with open("tests/out/test_" + str(index) + ".out", 'w') as f:
        for line in tmp_content:
                f.write(line)
    
    os.remove("tests/out/tmp_" + str(index) + ".out")

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

print('**************** TASK 01 COMPLETED *********************')