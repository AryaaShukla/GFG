class Solution:
    def myAtoi(self, s):
        s = s.lstrip()
        if not s:
            return 0
        sign, i, result = 1,0,0
        if s[0] in '+-':
            sign = -1 if s[0] == '-' else 1
            i =i+1
        while i <len(s) and '0' <= s[i] <= '9':
            result = result * 10 + (ord(s[i]) - ord('0'))
            i = i+1
        result = result * sign
        return max(-2**31,min(2**31-1,result))