# 0, 1, 1, 2, 3, 5, 8, 13, 
# fibonacci(0) == 0, fibonacci(1) == 1, fibonacci(2) == 1, etc.
def fibonacci(n):
    starter_array=[0,1]
    i=0
    j=1
    for item in list(range(n)):
        starter_array.append(starter_array[i]+starter_array[j])
        i+=1
        j+=1
    return starter_array[n]


print(fibonacci(4))
# print(list(range(7)))