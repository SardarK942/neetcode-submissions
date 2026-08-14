class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ''' 
        position[i] - postition of ith car in miles 
        speed[i] - speed of the ith car 
        
        destention is target param

        so bascially we need to simply 
        determine what the numbers will be at the end when the cars reach the target

        for example
        target = 10 miles
        position = [1, 4]
        speed = [3, 2]

        car at postion 1 mile goes at a speed 3mph
        car at position 4 goes at speed 2mph

        time = (target - position) / speed 

        bascially if car[0] has a smaller time than car[0] they will be the same fleet 
    '''
        stack = []
        cars = sorted(zip(position, speed), reverse=True)

        for pos, spd in cars:
            time = (target-pos)/ spd
            if not stack or stack[-1] < time: 
                stack.append(time)
        
        return len(stack)


            



