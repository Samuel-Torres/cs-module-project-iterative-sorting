def linear_search(arr, target):
    current_index = 0
    for i in arr:
        if i == target:
            return current_index
        else:
            current_index += 1
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle_index = (start + end) // 2
        val_at_middle = arr[middle_index]
        if val_at_middle == target:
            return middle_index
        if val_at_middle > target:
            end = middle_index - 1
        else:
            start = middle_index + 1

    return -1  # not found
