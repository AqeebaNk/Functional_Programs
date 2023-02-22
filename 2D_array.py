import numpy as np

def D2_array():

    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of colomn: "))

    arr = np.arange(1,(m*n)+1).reshape(m,n)
    print(arr)


D2_array()    