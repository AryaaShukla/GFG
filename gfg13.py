class Solution:
    def missingNumber(self, arr):
        n = len(arr)

        # Step 1: Place each number in its correct index
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                correct_idx = arr[i] - 1
                arr[i], arr[correct_idx] = arr[correct_idx], arr[i]

        # Step 2: Identify the missing number
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1

        return n + 1
