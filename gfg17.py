class Solution:
    def nonRepeatingChar(self,s):
        frq = {}
        for ch in s:
            if ch in frq:
                frq[ch] += 1
            else:
                frq[ch] = 1
                
        for chr in s:
            if frq[chr]==1:
                return chr
        return "$" 