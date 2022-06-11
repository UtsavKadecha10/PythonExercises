"""
Input = integer n
for n=4
Output Boolean variable = True/False:
True
*
**
***
****

False
****
***
**
*
"""

"""SOLUTION"""
"""Boolean Star Pattern"""

print("Enter n")
n=int(input())
print("Enter Boolean character")
i=bool(input())
if i:
    for x in range(1, n+1):
        for n in range(x):
            print("*", end="")
else:
    for x in range(n, 0, -1):
        for n in range(x):
            print("*", end="")    
print("\n")
