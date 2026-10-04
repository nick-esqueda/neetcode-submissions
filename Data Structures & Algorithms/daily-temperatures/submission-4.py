class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        When is the new high? / How many days till next high?


        "is there anything greater than this one?"
        "there isn't a new high after this one"
        "... but this would be a new high, so track it"
        
        "pop X times, X = num it takes till top of stack is greater than i"
        X is the result at i
        "if i is greater than top of stack, replace"
        "stack top is always the next biggest"
        stack [(40, 5), (38, 1), (30, 0)]
        [30,38,30,36,35,40,28]
          i
        [ 0  4  1  2  1  1  0]

        """
        # Holds the next biggest num
        # Replace when you find a num greater than top of stack
        stack = [(temperatures[-1], len(temperatures) - 1)] # (40, 5)
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1):
            num = temperatures[i]

            # Pop from stack until top is bigger than num
            while len(stack) > 0 and num >= stack[-1][0]:
                stack.pop()
            
            if len(stack) > 0:
                result[i] = stack[-1][1] - i

            stack.append((num, i))

        return result