nums = [4, 6, 2, 3, 1, 9, 7]


def merge(arrA, arrB):

    results = []
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] <= arrB[0]:
            results.append(arrA.pop(0))
        else:
            results.append(arrB.pop(0))

    return results + arrA + arrB


def merge_sort(arr):
    # base case
    if len(arr) < 2:
        return arr
    middle = round(len(arr) / 2)
    arrR = arr[0:middle]
    arrL = arr[middle:]
    return merge(merge_sort(arrR), merge_sort(arrL))


print(merge_sort(nums))
# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
# TO-DO

# return arr


# def merge_sort_in_place(arr, l, r):
# TO-DO

# return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort(arr):

#     return arr
