import math as mp
mid_no = 0
def middle(array2):
     if len(array2) > 1: 
        if (len(array2)%2) == 0:
          middler = (len(array2)/2)
          print('middle even: ', middler)
          return int(middler)
        else:
          middler = (mp.floor((len(array2)/2)) +1)
          print('middle: ', middler)
          return int(middler)
     else:
         middler=0
         return middler
        
           

def binary_search(array1, search_no):
        mid_no = middle(array1)
        print('mid_no ',mid_no )
        if mid_no != 0:
            if array1[mid_no] > search_no:
                #exclude mid_no 
                array1 = array1[:mid_no]
                print('New array:', array1)
                binary_search(array1, search_no)
            elif array1[mid_no] < search_no:
                array1 = array1[mid_no:]
                print('New array:', array1)
                binary_search(array1, search_no)
            else :
                print('Number found at index:',array1[mid_no])
        else:
            print('Number not found')

#Example usage:
array1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19,20]
search_no = 17
#function call
binary_search(array1, search_no)
middle(array1)

