class Solution:
    def pushZerosToEnd(self, arr):
        l = 0
        for r in range(len(arr)):
            if arr[r] != 0:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
        return arr
