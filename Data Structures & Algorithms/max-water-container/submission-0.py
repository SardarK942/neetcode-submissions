class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ''' 
        so this seems like a pretty simple problem of classing two pointers we iterate the side that is less - maintain max that's it 
''' 

        left = 0
        right = len(heights)-1
        res = -1
        while left < right: 
            leftH = heights[left]
            rightH = heights[right]
            vol = min(leftH, rightH) * (right-left)
            res = max(res, vol)
            
            if leftH < rightH:
                left +=1
            else:
                right -=1
            
        return res