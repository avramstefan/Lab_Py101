#!/usr/bin/python3

import os
from task03 import func

# Task 01
print('****************  TASK 03 STARTED  *********************')

path = os.getcwd() + "/tests/out"
try:
    os.mkdir(path)
except OSError:
    print(end = "")

lines = []
with open("tests/in/test.in") as f:
    lines = f.readlines()

decoded_message = lines[0]
coded_message = func(decoded_message)
    
write_file = "tests/out/test.out"
g = open(write_file, "w")
g.write(coded_message)
g.close()

out_file = "tests/out/test.out"
ref_file = "tests/ref/test.ref"

out_content = open(out_file).readlines()
ref_content = open(ref_file).readlines()

if out_content == ref_content:
    print("TASK 02.............................. PASSED")
else:
    print("TASK 02.............................. FAILED")

print('**************** TASK 03 COMPLETED *********************')