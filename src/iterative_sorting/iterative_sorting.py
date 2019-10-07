# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        for index in range(cur_index, len(arr)):
            if arr[index] < arr[smallest_index]:
                smallest_index = index
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    keep_sorting = True
    while keep_sorting:
        keep_sorting = False
        for index, element in enumerate(arr[:-1]):
            if element > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                keep_sorting = True
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

