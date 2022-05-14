"""Exercise-6"""
#Health Management System
# 2 clients - Harry, Rohan.
# Total 4 files.
# Write a function that when executed takes as input client name.
# Diet
# Timestamps in [] then whatever they ate
# Exercise
# Timestamps in [] then whatever exercise they did
# 2nd function to retrieve exercise food or client

"""SOLUTION"""
"""Health Management System"""

def getdate():
    import datetime
    return datetime.datetime.now()
    
def log(k):
    if k == 1:
        c = int(input("Press 1: Diet\nPress 2: Exercise\n"))
        if c == 1:
            value = input("Type here\n")
            with open("harry_diet.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully Updated\n")
        if c == 2:
            value = input("Type here\n")
            with open("harry_exercise.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully Updated\n")
        else:
            print("Invalid Input")
    if k == 2:
        c = int(input("Press 1: Diet\nPress 2: Exercise\n"))
        if c == 1:
            value = input("Type here\n")
            with open("rohan_diet.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully Updated\n")
        if c == 2:
            value = input("Type here\n")
            with open("rohan_exercise.txt", "a") as op:
                op.write(str([str(getdate())]) + ": " + value + "\n")
            print("Successfully Updated\n")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
def retrieve(k):
    if k == 1:
        c = int(input("Press 1: Diet\nPress 2: Exercise\n"))
        if c == 1:
            with open("harry_diet.txt") as op:
                for i in op:
                    print(i, end="")
        if c == 2:
            with open("harry_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        else:    
            print("Invalid Input")
    if k == 2:
        c = int(input("Press 1: Diet\nPress 2: Exercise\n"))
        if c == 1:
            with open("rohan_diet.txt") as op:
                for i in op:
                    print(i, end="")
        if c == 2:
            with open("rohan_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
                    
print("HEALTH MANAGEMENT SYSTEM")
a = int(input("Press 1: to log data\nPress 2: to retrieve data\n"))
if a == 1:
    b = int(input("Press 1: Harry\nPress 2: Rohan\n"))
    log(b)
if a == 2:
    b = int(input("Press 1: Harry\nPress 2: Rohan\n"))
    retrieve(b)
else:
    print("Invalid Input")
