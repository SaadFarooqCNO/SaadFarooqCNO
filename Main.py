def n_choose_k():

    n = int(input("Enter the first number (n): "))
    k = (int(input("Enter the second number (k): ")))

    if k == 0 or n == 0:
        return 1
    
    result = 1 
    for i in range(k):
        result *= n - i
        result //= i + 1
    
    print("{0} choose {1} = {2}".format(n,k,result))

    another_calc = input("Do you want to calculate more? (y,n) ")
    if another_calc in ["y"]:
        return n_choose_k()
    else:
        print("Finished!")

n_choose_k()