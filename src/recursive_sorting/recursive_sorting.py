# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    to_sort = list(arrA + arrB)
    for index, element in enumerate(merged_arr):
        min_element = None
        for element_to_sort in to_sort:
            if min_element is None or min_element > element_to_sort:
                min_element = element_to_sort
        merged_arr[index] = min_element
        to_sort.remove(min_element)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = (len(arr) // 2)
    arrA = arr[:mid]
    arrB = arr[mid:]
    arrA = merge_sort(arrA)
    arrB = merge_sort(arrB)

    return merge(arrA, arrB)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


arr = [1, 4, 2, 9, 48, 21, 34, 12, 18, 7, 5, 3]
print(merge_sort(arr))
