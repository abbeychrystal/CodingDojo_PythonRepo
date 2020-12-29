def selectionSort(lst):
    for i in range(len(list)-2):
        for j in range(1,i+1,1):
            if list(i)<list(j):
                list(i) = list(j)
    return lst

lst = [5,4,3,2,1]
print(selectionSort(lst))
            

