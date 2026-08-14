class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        sorted list - this has to be binry search !
        left pointer - right 

        if more than target move right -1 vice versa 
        ''' 

        l, r = 0, len(numbers)-1

        while l < r: 
            tot = numbers[l] + numbers[r]
            if tot == target: 
                return [l+1, r+1]
            
            if tot < target: 
                l +=1
            else:
                r -=1
        


