'''
Created by Adriano S. on 1/18/17
Displays an employees weekly pay
'''

def takeInput():
    hourWage = input("Enter Hourly Wage: ")
    hoursWorked = input("Enter Hours Worked: ")
    overtime = input("Enter Overtime Hours Worked: ")

    try:
        hourWage = float(hourWage)
        hoursWorked = float(hoursWorked)
        overtime = float(overtime)
        if(hourWage < 0 or hoursWorked < 0 or overtime < 0):
            print("You can't enter negative numbers.")
        else:
            print("The employee's paycheck amounts to", (hoursWorked*hourWage) + (overtime*(1.5*hourWage)),"USD.")
    except ValueError:
        print("Some of the input is invalid. Please use only numbers.")

takeInput()