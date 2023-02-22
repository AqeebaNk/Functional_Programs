import math
def windchill():
    temp = int(input("Enter the temp in Celcius:"))
    speed = int(input("Enter the speed in kilometer :"))
     
    t = temp + 32
    v = speed * 0.612

    print("\n",t,"Farenheit")
    print(v,"miles\n")

    formula = (13.12 + 0.615 * t - 11.37 * v ** 0.16 + 0.396 * t * v ** 0.16)

  

    if ( t > 50 or v >= 120):
        print("Enter the valid number")
    else:
          print(formula,"Farenheit")

windchill()    