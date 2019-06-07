#https://medium.com/basecs/counting-linearly-with-counting-sort-cd8516ae09b3
# Counting sort
# Time complexity O(n+k) 
# n size of array
# k range of integers in n


def counting_sort(arr):
    count = [0] * 10 # array to store the count of each numcounter
    c = [0] * len(arr) # c is the sorted array
    
    # store count of each number of arr in count
    for i in arr: 
        count[i] = count[i] + 1
    
    
    # cumulatively add the counts
    for i in range(1,len(count)):
        count[i] = count[i] + count[i-1]
        
    # shift count to the right 
    for i in range(len(count)-1,-1,-1):
        count[i] = count[i-1]
    count[0] = 0

    
    
    # consult arr and count to fill in array c
    for i in range(len(arr)):
        c[count[arr[i]]] = arr[i]
        count[arr[i]] = count[arr[i]] + 1
    
    

    print(c)


a = [9, 4, 1, 7, 9, 1, 2, 0]
counting_sort(a)

