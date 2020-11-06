def sequential_search(listNums, target):
    for i in range(len(listNums)):
        if listNums[i] == target:
            print(target + "found at " + i)

def binary_search(listNums, target, low, high):
    mid = (low + high)/2
    if high < low:
        return -1
    elif listNums[mid] == target:
        return target + "found at " + mid
    else:
        binary_search(listNums, target, low, mid)
        binary_serach(listNums, target, mid + 1, high)

def bubble_sort(listNums):
    n = listNums.len()
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if listNums[j] > listNums[j+1]:
                temp = listNums[j]
                listNums[j] = listNums[j+1]
                listNums[j+1] = temp

def selection_sort(listNums):
    n = listNums.len()
    for i in range(0, n-1):
        min_index = i
        for j in range(i+1, n):
            if listNums[j] < listNums[min_index]:
                min_index = j
        temp = listNums[min_index]
        listNums[min_index] = listNums[i]
        listNums[i] = temp

def insertion_sort(listNums):
    n = listNums.len()
    for i in range(1, n):
        key = listNums[i]
        j = i-1
        while j>= 0 and listNums[j] > key:
            listNums[j+1] = listNums[j]
            j = j-1
        listNums[j+1] == key