class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ''' Binary search I think it works where there's a l and r and m is calculated you check if that is the target - then return else if less than target then make left middle +1 and then I think if more make riught middle -1 ''' 

        l = 0
        r = len(nums)-1

        while l <= r: 
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            if nums[mid] < target: 
                l = mid+1
            else:
                r = mid-1
        
        return -1
