class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        stack [(40, 5), (28, 6)  ]
        [30,38,30,36,35,40,28]
                              i
        [ 1  4  1  2  1      ]
        """
        
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # If you come across a temp that is greater than top of stack,
            # then you found the hotter day for those waiting on the stack.
            # Compute the num days for those & put in result.
            while stack and temp > stack[-1][0]:
                topNum, topIdx = stack.pop()
                result[topIdx] = i - topIdx
            
            stack.append((temp, i))

        return result