class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        if len(s1) != len(s2):
           return False
        if sorted(s1) != sorted(s2):
            return False
        return s2 in (s1 +s1)  