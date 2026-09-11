class Solution:
    def isValid(self, s: str) -> bool:
        """
        if you come across an ending bracket, then check if it's associated start is at top of stack
        if doesn't match, return False
        if it does, just pop off the last of stack

        "[](){}"
          i

        stack = [ [,   ]
        
        
        """

        if len(s) % 2 != 0:
            return False
        
        parens = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []
        for c in s:
            if c in parens:
                # Return False if the top of the stack is not the matching open paren
                if not len(stack) or parens[c] != stack[-1]:
                    return False
                
                # Pop off the top of the stack - we found it's associated paren
                stack.pop()
            else:
                # Add open paren to stack
                stack.append(c)
 
        return len(stack) == 0