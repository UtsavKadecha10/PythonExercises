"""Exercise - 3"""
"""Guess the number"""
"""
Q. To write a program having a no. in it already, and allowing the user to input a no. and then the program responding
by telling if the no. he entered is equal to, greater than or lesser than the given no. within a limited amount of 
guesses(telling the no. of guesses left, or the no. of guesses in which he finished it, and also using game over on 
loosing and won on winning).
"""

"""SOLUTION"""
"""Guess the number"""

print("Number of chances available = 5")
i=5
print("# NEW GAME")
print("------------------------------------------------------")
print("Enter you name")
b = input()
print("Enter a number between 10 and 30")
a = int(input())
n = i
while(True):
    if (a==20):
        print("You won\nCongratulations")
        break
    else:
        print("Try again")
        print("You`ve", n-1, "chances left")
        print("Enter a number between 10 and 30")
        a=int(input())
        n = n - 1
        if(n==1):
            print("Game over")
            break
