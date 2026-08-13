class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
       first num off the board get's 
        '''
        numstack = []
        opstack = []
        operands = ['+', '-', '*', '/']
        for item in tokens: 
            if item not in operands:
                numstack.append(int(item))
            else: 
                temp = None
                if item == '+':
                    temp = numstack.pop() + numstack.pop()
                if item == '-': 
                    secondNum = numstack.pop()
                    temp = numstack.pop() - secondNum
                if item == '*':
                    temp = numstack.pop() * numstack.pop()
                if item == '/':
                    secondNum = numstack.pop()
                    temp = int(numstack.pop() / secondNum)
                
                numstack.append(temp)

        return int(numstack.pop())
       

                         

