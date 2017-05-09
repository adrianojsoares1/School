from math import pi

def sphereFunctions():
    radius = (input("Radius: "))
    try:
        radius = float(radius)
        if radius >= 0.0:
            print("The diameter is",radius*2)
            print("The circumference is",radius*2*pi)
            print("The surface area is",radius**2*pi*4)
            print("The volume is:",radius**3*pi*(4/3))
            print("Enter another positive value, or a negative value to exit.")
            sphereFunctions()
        else:
            print("You entered a negative number. Goodbye!")
    except ValueError:
        print("You may only enter numbers.")

sphereFunctions()