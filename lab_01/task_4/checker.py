#!/usr/bin/python3

import os
from task04 import func

# Task 01
print('****************  TASK 04 STARTED  *********************')

all_files = []
for index in range(1, 4):
    file_name = "tests/in/test_" + str(index) + ".in"
    all_files.append(file_name)

index = 1
for file in all_files:

    given_numbers_string = []
    with open(file) as f:
        given_numbers_string = f.readlines()
    input = given_numbers_string[0]
    input = input[1:len(input) - 1]
    given_numbers_split = input.split(",")
    given_numbers = (int(element) for element in given_numbers_split)
    nice_list = func(given_numbers)

    write_file = "tests/out/test_" + str(index) + ".out"
    g = open(write_file, "w")
    g.write(str(nice_list))
    g.close()

    index += 1

for test_case in range(1, 4):
    out_file = "tests/out/test_" + str(test_case) + ".out"
    ref_file = "tests/ref/test_" + str(test_case) + ".ref"

    out_content = open(out_file).readlines()
    ref_content = open(ref_file).readlines()

    if out_content == ref_content:
        print("TEST " + str(test_case) + ".............................. PASSED")
    else:
        print("TEST " + str(test_case) + ".............................. FAILED")

print('**************** TASK 04 COMPLETED *********************')