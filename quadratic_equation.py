from cmath import sqrt

def Qadratic():
    a = int(input("Enter the Valve of a: "))
    b = int(input("Enter the Valve of b: "))
    c = int(input("Enter the Valve of c: "))

    delta = (b * b) - (4 * a * c  ) 

    root1 = (-b + sqrt (delta))/ (2 * a)
    root2 = (-b - sqrt (delta))/ (2 * a)

    print(root1,root2)


Qadratic()