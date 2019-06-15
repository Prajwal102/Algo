
def subset_sum(arr, n, sum):
    if(sum == 0):
        return True
    if(n < 0 or sum < 0):
        return False
    
    a = subset_sum(arr, n-1, sum - arr[n]) #include curent elem and recurse n-1 elems for sum-n

    b = subset_sum(arr, n-1, sum) # or dont include current elem and recurse n-1 elems

    return (a or b)


if(__name__ == "__main__"):
    arr = [3, 34, 4, 5, 12, 2]
    n = len(arr)
    sum = 1
    if(subset_sum(arr ,n-1 , sum)):
        print("yes")
    else:
        print("no")
        