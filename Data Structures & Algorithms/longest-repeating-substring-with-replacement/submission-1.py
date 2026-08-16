class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        l = 0
        res = 0
        max_count = 0

        for r in range(len(s)): 
            counts[s[r]] += 1
            max_count = max(max_count, counts[s[r]])
            while (r-l +1) - max_count > k:
                counts[s[l]] -= 1
                l += 1
            res = max(res, (r-l)+1)

        return res

