def bubble_sort(list):
    for i in range (len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list 


print(bubble_sort([40,22,6,15,3,54]))