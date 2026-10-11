class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Need to know rules for valid parens

        n = 3
        ()()(), (())(), ()(()), (()()), ((()))
        
        "which paren goes in this spot?"
        each valid combo has (n * 2) length

        [_, _, _, _, _, _]
         i

        - decide to put start or end paren in spot
            - BUT, must make sure is valid to do so
        - track of "due" parens, e.g., number of end parens that need to be put
            - aka rules need to be followed
        in spot X, you have options, but need to figureo out what options:
            - can only put start paren if num starts < n
            - can only put an ending paren when there's a corresponding open paren
                - aka num open parens > num close parens?
        
        0, 2, 4 in between ( and )
        """
        
        allParens = []
        def backtrack(curr, numStarts, numEnds):
            if numStarts >= n and numEnds >= n:
                allParens.append(curr)
                return

            # Choose Open
            if numStarts < n:
                backtrack(curr + "(", numStarts + 1, numEnds)

            # Choose Close
            if numEnds < numStarts:
                backtrack(curr + ")", numStarts, numEnds + 1)
        
        backtrack("", 0, 0)
        return allParens