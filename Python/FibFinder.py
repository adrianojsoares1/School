"""
Adriano Soares
1/25/2017
Quiz 1
"""

'''QUESTION 1'''


def fibrecurve(a, b, num):
    if a < num:
        fibrecurve(b, a+b, num)
    elif a == num:
        print(num, "is in the fibonacci sequence!")
    else:
        print(num, "is not in the fibonacci sequence.")


def fibloop(num):
    a, b = 0, 1
    while a < num:
        a, b = b, a+b
    if a == num:
        print(num, "is in the fibonacci sequence!")
    else:
        print(num, "is not in the fibonacci sequence.")

#number = int(input("Enter a number:"))
print("Recursive Algorithm says:")
#fibrecurve(0, 1, number)
print("\nLooping Algorithm says:")
#fibloop(number)

'''END QUESTION 1 | BEGIN QUESTION 2'''


def reverseR(string):
    if len(string) == 0:
        return string
    return string[len(string)-1:] + reverseR(string[:-1])
def reverseL(string):
    temp = ""
    length = len(string)
    for i in range(0, length):
        temp += string[(length - i - 1): (length - i)]
    return temp
def simplereverse(string):
    return string[::-1]

print("\nOriginal String says: We are number one")
print("Recursive algorithm says:", reverseR("We are number one"))
print("Looping algorithm says:", reverseL("We are number one"))
print("Simple algorithm says:", simplereverse("We are number one"))

'''END QUESTION 2 | BEGIN QUESTION 3'''


def remainder(num, denom):
    if denom == 0:
        return "Error: Div by 0!"
    if num < denom:
        return num
    else:
        return remainder((num-denom), denom)


def remainderLoop(num, denom):
    if denom == 0:
        return "Error: Div by 0!"
    while num < denom:
        num -= denom
    return num

dividend = int(input("\nEnter dividend:"))
divisor = int(input("Enter divisor:"))
print("\nThe remainder of", dividend, "and", divisor, "is:", remainder(dividend, divisor), "via recursive algorithm")
print("The remainder of", dividend, "and", divisor, "is:", remainder(dividend, divisor), "via looping algorithm")

'''END PROBLEM 4 | BEGIN PROBLEM 5'''

