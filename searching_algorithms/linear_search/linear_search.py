search_array = [1,2,3,4,5,6,7,8,9,10]
search_no = 13
for n in range(0,len(search_array)):
    if search_array[n] == search_no:
       print('Found at ', n)
       break
    elif n == (len(search_array)-1):
       print('Not Found in array')
     
