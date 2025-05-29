class Solution:
    def inversionCount(self, arr):
        n = len(arr)
        temp = [0]*n
        return self.merge_sort(arr, temp, 0, n-1)

    def merge_sort(self, arr, temp, l, r):
        inv_count = 0
        if l < r:
            mid = (l + r) // 2
            inv_count += self.merge_sort(arr, temp, l, mid)
            inv_count += self.merge_sort(arr, temp, mid + 1, r)
            inv_count += self.merge(arr, temp, l, mid, r)
        return inv_count

    def merge(self, arr, temp, l, mid, r):
        i, j, k = l, mid + 1, l
        inv_count = 0
        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j <= r:
            temp[k] = arr[j]
            j += 1
            k += 1

        for idx in range(l, r + 1):
            arr[idx] = temp[idx]

        return inv_count
