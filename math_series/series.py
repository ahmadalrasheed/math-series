# 0, 1, 1, 2, 3, 5, 8, 13, 
# fibonacci(0) == 0, fibonacci(1) == 1, fibonacci(2) == 1, etc.
def fibonacci(n):
    """
    this function generates a series of fibunacci numbers
    0, 1, 1, 2, 3, 5, 8, 13, ...
    """
    starter_array=[0,1]
    i=0
    j=1
    for item in list(range(n)):
        starter_array.append(starter_array[i]+starter_array[j])
        i+=1
        j+=1
    return starter_array[n]

def lucas(n):
    """
    this function generates a series of lucas numbers
    2, 1, 3, 4, 7, 11, 18, 29, ...
    """
    starter_array=[2,1]
    i=0
    j=1
    for item in list(range(n)):
        starter_array.append(starter_array[i]+starter_array[j])
        i+=1
        j+=1
    return starter_array[n]

def sum_series(n,num1=0,num2=1):
    """
    this function generates a series of fibonacci numbers by default
    2, 1, 3, 4, 7, 11, 18, 29, ...
    but if you entered the second and teh third argument as 2, 1 it will generate lucas series 
    and if you entered the second and teh third argument as two random numbers it will generate a series depending on this numbers
    """ 
    starter_array=[num1,num2]
    i=0
    j=1
    for item in list(range(n)):
        starter_array.append(starter_array[i]+starter_array[j])
        i+=1
        j+=1
    return starter_array[n]  

# print(fibonacci(4))
# print(list(range(7)))