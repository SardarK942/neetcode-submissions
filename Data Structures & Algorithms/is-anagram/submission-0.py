class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        We have string s and t 
        Will they always be the same length? or is that an edge case we want to cover? 
        Is it case sensitve? 

        We will sort both strings - and then compare each index as we move through the string 
        this would be O(log(n)n + log(m)m) and 0 (1 space)
        

        --- 

        Better solution would be to jsut get the count of each letter the numebr of times it gets counted - since 
        """
        if len(s) != len(t): 
            return False
        counts = {}
        
        for char in s: 
            counts[char] = counts.get(char, 0) + 1
        
        for char in t: 
            if char not in counts: 
                return False

            counts[char] = counts.get(char) - 1
            if counts[char] == -1:
                return False
        
        return True






