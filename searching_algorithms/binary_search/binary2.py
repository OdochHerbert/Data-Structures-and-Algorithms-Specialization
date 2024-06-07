##RADOM SEARCH
import random

def binary_search(array1, search_no):
        rand_no = random.randint(0, 19)
        print('Search number:', rand_no)
        if rand_no > search_no:
            array1 = array1[:rand_no]
            print('New array:', array1)
            binary_search(array1, search_no)
        elif rand_no < search_no:
            array1 = array1[rand_no:]
            print('New array:', array1)
            binary_search(array1, search_no)
        elif rand_no == search_no :
            print('Number found at index:')

#Example usage:
array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19]
search_no = 5
#function call
binary_search(array1, search_no)
