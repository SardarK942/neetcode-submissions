class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        we make a left pntr and right pntr 
        and bring inside one by one if we find a diff return false if we become same index or pass each other then return true 
        '''
        clean = "".join(c for c in s if c.isalnum()).lower()
        left = 0
        right = len(clean)-1
        while left < right: 
            if clean[left] != clean[right]: 
                return False
            left+=1
            right-=1
        return True