def circularSubarraySum(arr):
    tot = sum(arr)
    max_end = min_end = max_sum = min_sum = arr[0]
    
    for num in arr[1:]:
        max_end = max(num, max_end + num)
        max_sum = max(max_sum, max_end)

        min_end = min(num, min_end + num)
        min_sum = min(min_sum, min_end)
        
    if max_sum < 0:
        return max_sum
        
    return max(max_sum, tot - min_sum)