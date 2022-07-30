import os
from task03 import func

# Task 01
print('****************  TASK 02 STARTED  *********************')

lines = []
with open("input/input.txt") as f:
    lines = f.readlines()

decoded_message = lines[0]
coded_message = func(decoded_message)
    
write_file = "output/out.txt"
g = open(write_file, "w")
g.write(coded_message)
g.close()

out_file = "output/out.txt"
ref_file = "ref/ref.txt"

out_content = open(out_file).readlines()
ref_content = open(ref_file).readlines()

if out_content == ref_content:
    print("TASK 02.............................. PASSED")
else:
    print("TASK 02.............................. FAILED")

print('**************** TASK 02 COMPLETED *********************')