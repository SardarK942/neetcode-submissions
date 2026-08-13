class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ''' 
        I would go to each day and set start i and tne I would keep i++ing until i is a hotter temp and then subtract that end - start and set that for i it would be a double for loop 
        initialize result list with all 0's 
        We add index to stack 
        we check if it is more than - it is 
        '''
        result = [0] * len(temperatures)
        stack = []
        for i, currtemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < currtemp: 
                j = stack.pop()
                result[j] = (i - j)
            stack.append(i)
        return result
        