class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        if len(s1) != len(s2):
            return False
        count1 = {}
        count2 = {}
        for c1,c2 in zip(s1,s2):
            count1[c1] = count1.get(c1,0)+1
            count2[c2] = count2.get(c2,0)+1
        return count1 == count2    