class Solution:
	def maxProduct(self,arr):
		n = len(arr)
		max_pr = arr[0]
		curr_max,curr_min = arr[0],arr[0]
		for i in range(1,n):
			if arr[i]<0:
				curr_max,curr_min = curr_min,curr_max
				curr_max = max(arr[i],curr_max*arr[i])
				curr_min = min(arr[i],curr_min*arr[i])
				max_pr = max(max_pr,curr_max)
		return max_pr 