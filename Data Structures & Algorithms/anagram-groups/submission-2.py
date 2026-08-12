class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        This problem is honeslty easier than it actually is but i think we may have to brute approach 
        Use a hashmmap: Sorted String -> list of Strings 
        We are going to iterate through the list and sort the string and then add it to the list 
        """
        anagramMap = defaultdict(list)
        for word in strs: 
            sortedWord = "".join(sorted(word))
            anagramMap[sortedWord].append(word)
        return list(anagramMap.values())
        
