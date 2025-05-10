def sumarr(arr):
    max_curr = max_glob = arr[0]
    for i in range(1,len(arr)):
        max_curr = max(arr[i],max_curr+arr[i])
        max_glob = max(max_glob,max_curr)
    return max_glob    