class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Using a hashset we'll check if dupes etc 
        but my question is how do we maintain the window? - start and end and then wehn we find a dupe do we restart the count starting at start+1? 
        ''' 
        l = 0
        seen = set()
        longest = 0
        for r in range(len(s)):
            while s[r] in seen: # remove left most until duplicate is gone 
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            longest = max(longest, r-l +1)
        return longest
