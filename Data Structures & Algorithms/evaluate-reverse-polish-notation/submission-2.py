from math import trunc

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        normal: 1 - 2 x 3 = -5
        RPN:    1 2 3 x - = -5

        ["1", "2", "3", "x", "-"]

        ["1","2","+","3","*","4","-"]

        tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        tokens=["10","6","-132","/","*","17","+","5","+"]


        Iterate through tokens
        When you hit an operand, solve the equation (operand and last two indices)
        Replace the prev indexes with the result? Feels weird, inefficient
        Replace the operand idx with the result?
        Put the result on a stack? Because need to use it later?
        - stack is a holding area for all nums
        - when cross an operator, solve the two at top of stack - will replace the top, so it's ready for the next operation
        """

        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: trunc(x / y),
        }
        stack = []

        for token in tokens:
            if token in operations:
                # Operator
                op2 = stack.pop()
                op1 = stack.pop()
                result = operations[token](op1, op2)
                stack.append(result)
            else:
                # Normal number
                stack.append(int(token))
        
        return stack[-1]



        