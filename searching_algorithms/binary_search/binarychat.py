def middle(array2):
    return len(array2) // 2

def binary_search(array1, search_no):
    if len(array1) == 0:
        print('Number not found')
        return False
    
    mid_no = middle(array1)
    if array1[mid_no] == search_no:
        print('Number found at index:', array1[mid_no])
        return True
    elif array1[mid_no] > search_no:
        return binary_search(array1[:mid_no], search_no)
    else:
        return binary_search(array1[mid_no + 1:], search_no)

# Example usage:
array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20]
search_no = 20
# function call
binary_search(array1, search_no)
