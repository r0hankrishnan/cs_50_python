import sys

# #Run file by writing "python ./lecture-4/name.py Rohan"
# print("hello, my name is", sys.argv[1])

if len(sys.argv) < 2:
    print("Too few args")
elif len(sys.argv) >2:
    print("Too many args")
else:
    print("hello, my name is", sys.argv[1])