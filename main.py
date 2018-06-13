from script import Script
import sys

if len(sys.argv) == 2:
    Script.run(sys.argv[1])
elif len(sys.argv) == 1:
    Script.run(input("please enter the filename of an mdl script file: \n"))
else:
    print("Too many arguments.")
