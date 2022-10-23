import os
import shutil
from task01a import task1a
from task01b import task1b
from task01c import task1c

def output_dir(task_nr):
    try:
        os.mkdir(f"tests/task01{task_nr}/out/")
    except:
        shutil.rmtree(f"tests/task01{task_nr}/out/")
        os.mkdir(f"tests/task01{task_nr}/out/")

def final_check(task_nr):
    solved = 1
    for test_case in range(1, 6):
        out_file = f"tests/task01{task_nr}/out/test_" + str(test_case) + ".out"
        ref_file = f"tests/task01{task_nr}/ref/test_" + str(test_case) + ".ref"

        out_content = open(out_file).readlines()
        ref_content = open(ref_file).readlines()

        if out_content == ref_content:
            print("TEST " + str(test_case) + " .............................. PASSED")
        else:
            solved = 0
            print("TEST " + str(test_case) + " .............................. FAILED")

    if solved:
        print(f'**************** TASK 01{task_nr} COMPLETED ********************')
    else:
        print('******************* FAILED TESTS ***********************')


# Task 01a
output_dir("a")
print('****************  TASK 01a STARTED  ********************')

all_files = []
for index in range(1, 6):
    file_name = "tests/task01a/in/test_" + str(index) + ".in"
    all_files.append(file_name)

index = 1
for file in all_files:
    with open(file) as f:
        lines = f.read()

    nums_string = lines.split(" ")
    nums = [int(elem) for elem in nums_string]

    result = task1a(nums)

    write_file = "tests/task01a/out/test_" + str(index) + ".out"
    g = open(write_file, "w+")
    for elem in result:
        g.write(str(elem) + " ")
    g.close()

    index += 1

final_check("a")
print()

# Task 01b
output_dir("b")
print('****************  TASK 01b STARTED  ********************')

all_files = []
for index in range(1, 6):
    file_name = "tests/task01b/in/test_" + str(index) + ".in"
    all_files.append(file_name)

index = 1
for file in all_files:
    with open(file) as f:
        lines = f.read()

    result = task1b(lines)

    write_file = "tests/task01b/out/test_" + str(index) + ".out"
    g = open(write_file, "w+")
    g.write(result)
    g.close()

    index += 1

final_check("b")
print()

# Task 01c
output_dir("c")
print('****************  TASK 01c STARTED  ********************')

all_files = []
for index in range(1, 6):
    file_name = "tests/task01c/in/test_" + str(index) + ".in"
    all_files.append(file_name)

index = 1
for file in all_files:
    with open(file) as f:
        lines = f.read()

    words = lines.split(" ")
    result = task1c(words)

    write_file = "tests/task01c/out/test_" + str(index) + ".out"
    g = open(write_file, "w+")
    for elem in result:
        g.write(str(elem) + " ")
    g.close()

    index += 1

final_check("c")
