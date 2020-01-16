
arr = [4, 6, 2, 3, 1]


def selection_sort(arr):

    for i in range(0, len(arr) - 1):
        smallest_index = i
        for j in range(i, len(arr)):
            # out of range below
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    print(arr)
    return arr


selection_sort(arr)


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 2):
            if j < len(arr) - 1:
                if arr[j] > arr[j + 1]:
                    arr[j] = arr[j + 1]
    print(arr)
    return arr


bubble_sort(arr)

# STRETCH: implement the Count Sort function below
# def count_sort(arr, maximum=-1):

#     return arr
