'''
Created by Adriano S. on 1/18/17
Calculates Pi using the Leibniz approximation method
'''
def calcPi():
    iterations = input("Enter number of iterations:")
    try:
        iterations = int(iterations)
        addOrSub = False
        denom = 3
        result = 1
        for i in range(0,iterations):
            if addOrSub:
                result += (1/denom)
            else:
                result -= (1/denom)
            denom+=2
            addOrSub = not addOrSub
        print("Pi is approximately:",result*4)
    except ValueError:
        print("Invalid Input. Please enter only numbers.")
calcPi()