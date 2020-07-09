def insertion_sort(list):
    # the first element is already in the "sorted side"
    # (abstract idea, no code required)

    # for all other items, we should do things
    # starting at the second item, iterate until the end of the array
    for i in range(1, len(list)):
        # the current number at the index represents the value currently being sorted
        current_val = list[i]
        # move the current number back through the array ( to the "sorted side" )
        current_index = i
        # keep moving until: its greater than the number before it OR we reach the start of array
        while current_index > 0 and current_val < list[current_index-1]:
            # replace the current value with the one to left of it
            list[current_index] = list[current_index-1]
            current_index -= 1
        # set the value at the current index to the current number
        # at this moment, current_index represents the new location for the current number
        list[current_index] = current_val

    return list


print(insertion_sort([8, 4, 2, 5, 1, 3]))
