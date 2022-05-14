"""Exercise - 2"""
"""Faulty Calculator"""
"""45*3 = 555, 56+9 = 77, 56/6 = 4"""
"""
Q. Design a calculator which will correctly solve all the problems except" the following ones:-
45*3 = 555, 56+9 = 77, 66-10 = 46, 56/6 = 4.
Your program should take operator and the two numbers as input from the user and then return the result.
"""

"""SOLUTION"""
"""FAULTY CALCULATOR"""

while(True):
    print("Enter 1st number")
    a=input()
    print("Enter 2nd number")
    b=input()
    c=input("Choose the Operator (+,-,*,/,%) = ")
    if c=="+":
        if a=="56" and b=="9":
            print("Answer = 77")
            print("________________________________________________")
        elif a=="9" and b=="56":
            print("Answer = 77")
            print("________________________________________________")
        else:
            print("Answer =", int(a)+int(b))
            print("________________________________________________")
    elif c=="-":
        if a=="66" and b=="10":
            print("Answer = 46")
            print("________________________________________________")
        else:
            print("Answer =", int(a)-int(b))
            print("________________________________________________")
    elif c=="*":
        if a=="45" and b=="3":
            print("Answer = 555")
            print("________________________________________________")
        elif a=="3" and b=="45":
            print("Answer = 555")
            print("________________________________________________")
        else:
            print("Answer =", int(a)*int(b))
            print("________________________________________________")
    elif c=="/":
        if a=="56" and b=="6":
            print("Answer = 4")
            print("________________________________________________")
        else:
            print("Answer =", int(a)/int(b))
            print("________________________________________________")
    elif c=="%":
        print("Answer =", int(a)%int(b))
        print("________________________________________________")
    else:
        print("Error! Try Again.")
        print("________________________________________________")
        continue
