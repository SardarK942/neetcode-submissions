class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        we need to bascially find the min and then the max and if we find a better min on the way 
        '''
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        return max_profit