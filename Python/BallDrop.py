'''
Created by Adriano S. on 1/18/17
Displays the total distance traveled by a dropped bouncing object
'''
def calcDist():
    start = input("Starting Height:")
    try:
        start = float(start)
        dist = 0
        bounces = 0
        while start > 0:
            dist += + start + (start*.6)
            start -= (start*.6)
            bounces +=1
        print("The ball bounced a total of",bounces,"times and traveled a grand total of",("%.3f" % dist),"Meters.")
    except ValueError:
        print("The input is invalid. Please use only numbers")
calcDist()