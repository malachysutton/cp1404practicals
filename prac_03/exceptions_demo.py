"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When either the numerator or denominator are not valid numbers.
2. When will a ZeroDivisionError occur?
When one of the numbers entered by the user is zero because you cannot divide by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#1.
#2. A ZeroDivisionError will occur when one of the numbers entered by the user is zero.