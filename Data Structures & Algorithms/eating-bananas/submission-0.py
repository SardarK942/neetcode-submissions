import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        pile of bananas and a time limit h to eat those bananas 
        goal: what's the minimum rate of K to eat every pile of bananas in h hours 
        catch: you can only eat 1 pile in k time other words you cannot go to the next pile even if you have excess k 
        k = bananas per hour 

    1. sort arr 
    2. grab median 
    3. test median 
    4 repeat until binary search ends
    5. maintain min of all searches that pass test
    '''

        res = max(piles)
        l = 1 
        r = max(piles)

        while l <= r: 
            k = (l + r) // 2

            #test mid
            tot = 0
            for num in piles: 
                tot += math.ceil(num / k)
            
            if tot <= h: 
                res = min(k, res)
                r = k - 1
            else: 
                l = k +1 

        return res
