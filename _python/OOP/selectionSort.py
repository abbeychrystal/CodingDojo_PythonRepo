def selectionSort(lst):
    for i in range(len(lst)-2):
        for j in range(1,i+1,1):
            if lst(i)<lst(j):
                lst(i), lst(j) = lst(j), lst(i)
    return lst

lst = [5,4,3,2,1]
print(selectionSort(lst))
            

