class Solution:
    def hIndex(self, citations):
        n = len(citations)
        count = [0] * (n + 1)

        # Count citations
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1

        # Traverse from end to find H-index
        total = 0
        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i
        return 0