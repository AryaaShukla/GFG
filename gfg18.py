class Solution:
    def minChar(self, s):
        rev_s = s[::-1]
        combined = s + '#' + rev_s
        lps = [0] * len(combined)
        for i in range(1, len(combined)):
            length = lps[i - 1]
            while length > 0 and combined[i] != combined[length]:
                length = lps[length - 1]
            if combined[i] == combined[length]:
                length += 1
            lps[i] = length
        return len(s) - lps[-1]
