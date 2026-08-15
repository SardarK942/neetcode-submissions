class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ''' this problem is interesting 
        we have to first do binary search on first y axis find a num that is less than target 

then we do a binary seach on the x axis of the array we choose to find the number 
    ''' 

    # [1, 2, 4, 8]
    # [10, 11, 12, 13]
    # [14, 20, 30, 40]

    #Binary search on first [x][0]
        l = 0
        r = len(matrix) -1
        while l <= r: 
            mid = (r + l) // 2
            if matrix[mid][0] == target: 
                return True

            if matrix[mid][0] < target: 
                l = mid +1
            else:
                r = mid -1
        
        # r becomes the y axis [r][x]
        if r < 0:
            return False
        col = r
        l = 0
        r = len(matrix[0])-1
        while l <= r:
            mid = (r + l) // 2
            if matrix[col][mid] == target: 
                return True

            if matrix[col][mid] < target: 
                l = mid +1
            else:
                r = mid -1
        return False