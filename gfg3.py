class Solution:
    def findMajority(self, arr):
        n =len(arr)
        thresh = n //3
        count = {}
        result = []
        for x in arr:
            if x in count:
                count[x] +=1
            else:
                count[x] =1 
        for num in count:
            if count[num] > thresh:
                result.append(num)
        result.sort()
        return result