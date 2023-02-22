def sum_zero():

    arr = []
    n = int(input("Enter how many numbers you want to add : "))

    for i in range(n):
        ele = int(input(f"Enter the {i+1} value of list : "))
        arr.append(ele)


    n = len(arr)
    flag = False
    for i in range(n-2):#1
        for j in range(1,n-1):#0,-1,2
            for k in range(2,n):#-1,2,-2,,,,,-1,2,-2
                if((arr[i] + arr[j] + arr[k]) == 0):
                    print(arr[i],arr[j],arr[k])
                    flag = True

    if(flag!=True):
        print("The list does not have  combinations which gives sum of 3 integers equale to Zero")

sum_zero()

