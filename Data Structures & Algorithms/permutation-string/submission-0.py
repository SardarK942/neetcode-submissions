class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ''' 
        We need to perform a sliding window 
        for loop r 
        and while loop 
        Also we can only maintain a window 
        of the shortest element 

        now let's talk data structures 
        
        Should we maintain a count of each char - but how would we determine when we find the answer when the window has all the char counts of the the least - oh we can sort the string of every window 
        '''
        if len(s1) > len(s2):
            return False
        
        windowLen = len(s1)
        s1Count = [0] * 26
        windCount = [0] * 26
        

        for i in range(windowLen):
            s1Count[ord(s1[i]) - ord("a")] += 1 
            windCount[ord(s2[i]) - ord('a')] +=1
        
        for r in range(len(s1), len(s2)):
            if s1Count == windCount:
                return True
            windCount[ord(s2[r-windowLen])- ord('a')] -= 1
            windCount[ord(s2[r]) - ord('a')] += 1
        
        return s1Count == windCount

            

