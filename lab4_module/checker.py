#!/usr/bin/python3

import os, sys
from task01 import task01 as t1
from task02 import task02 as t2

def check_task1():
    input_files = []

    print('****************  TASK 01 STARTED  *********************')

    for i in range (1,11):
        input_files.append(f"task01/tests/in/{i}.in")
    i = 1
    for filename in input_files:
        input = open(filename, 'r')
        line = input.readline()
        numbers = line.split(' ')

        radius = float(numbers[0])
        x = float(numbers[1])
        y = float(numbers[2])

        x_res, y_res = t1.random_points(radius, x, y)

        if ((x_res - x) ** 2 + (y_res - y) ** 2) <= radius ** 2:
            print("TEST " + f"{i}" + ".............................. PASSED")
        else:
            print("TEST " + f"{i}" + ".............................. NOT PASSED")
        i += 1

        input.close()

def check_task_2_1():
    input_files = []

    print('****************  TASK 02.1 STARTED  *********************')

    for i in range (1,11):
        input_files.append(f"task02/tests/in/{i}.ppm")

    i = 1
    for filename in input_files:
        image = t2.Image()

        image.read(filename)
        
        input = open(filename, 'r')
        
        lines = ""
        for line in input.readlines():
            lines += line
        
        if image.to_string() == lines:
            print("TEST " + f"{i}" + ".............................. PASSED")
        else:
            print("TEST " + f"{i}" + ".............................. NOT PASSED")

        input.close()
        i += 1

def check_task_2_2():
    input_files = []
    print('****************  TASK 02.2 STARTED  *********************')
    for i in range (1,11):
        input_files.append(f"task02/tests/in/{i}.ppm")

    i = 1
    for filename in input_files:
        image = t2.Image()
        
        image.read(filename)

        image.sepia()
        image.write(f"task02/tests/out/{i}.ppm")
        
        output = open(f"task02/tests/out/{i}.ppm", 'r')
        ref_output = open(f"task02/tests/ref/{i}.ppm", 'r')
        if output.readlines() == ref_output.readlines():
            print("TEST " + f"{i}" + ".............................. PASSED")
        else:
            print("TEST " + f"{i}" + ".............................. NOT PASSED")
        output.close()
        ref_output.close()
        i += 1

if len(sys.argv) == 1:
    check_task1()
    check_task_2_1()
    check_task_2_2()
elif len(sys.argv) == 2:
    if sys.argv[1] == "1":
        check_task1()
    elif sys.argv[1] == "2":
        check_task_2_1()
        check_task_2_2()
    else:
        print("No valid arguments!")
elif len(sys.argv) == 3:
    if sys.argv[1] == "2":
        if sys.argv[2] == "1":
            check_task_2_1()
        elif sys.argv[2] == "2":
            check_task_2_2()
        else:
            print("No valid arguments!")
    else:
        print("No valid arguments!")
else:
    print("No valid arguments!")