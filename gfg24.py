class Solution:
    def mergeOverlap(self, arr):
        arr.sort(key=lambda x: x[0])
        merged = []
        for i in range(len(arr)):
            current = arr[i]
            if not merged or merged[-1][1] < current[0]:
                merged.append(current)
            else:
                merged[-1][1] = max(merged[-1][1], current[1])
        return merged
