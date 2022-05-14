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
"""Bool Star Pattern"""

print("Enter n")
n=int(input())
print("Enter Boolean character")
i=bool(input())
while(True):
    if i==True & 3<n<8:
        print((n-3)*"*")
        n=n+1
    if i==False & 3<n<8:
        print((n)*"*")
        n=n-1
