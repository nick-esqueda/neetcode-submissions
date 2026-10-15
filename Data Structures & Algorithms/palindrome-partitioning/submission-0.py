class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Want all UNIQUE (order) possible lists of substrings where each substr is a palindrome
        Need to return all strings, grouping the palindromes
        Must have the whole string in it

        Can't reorder chars
        Choose whether to include next char? Depending on if it's a palin
        But how to get all possible ones?
        Have to scan to see if eventually the substr could be a palin eventually

        OR, choosing where partition points are??
        "partition here, don't partition here, etc."
        like take/choose but on where you're partitioning/what you decide to include?

        don't include in res unless is a palindrome?

        is it like building multiple combos?

        moving two pointers, "is this a palindrrome, is this, is this"

        choose midpoint, go out with i/j until no longer palindrome?
        - won't work for even lengths though
        "if this letter doesn't make a palindrome, keep by itself"
        take/skip using as palindrome if could be one??
        "take/skip going outwards"

        find palindromes of length 1/2/3...?

        all = ["r", ]
        " r a c e c a r "
              i

        all = [["r", "a", "c", "e", "c", "a", "r"], ["r", "a", "c", "e]
        " r a c e c a r "
              i          
                  j          

        all = [["r", "a", "c", "e", "c", "a", "r"],  ["cec", "r", "a", "a", "r"], ["aceca", "r", "r"]]
        " r a c e c a r "
          i           j
        l = 6
        need to know when to not put a duplicate on there (e.g., no palindromes of size X, so)
        store all not used in the palindrome somehow? to append to list


        all = [["r", "a", "c", "e", "c", "a", "r"], ["r", "a", "c", "e]
        " r a c e c a r "
              i          
                  j          
        deciding what I to start on and start radiating out
        if it makes a palindrome going out, then decide to take it or make bigger
        dump the rest outside of those indexes into list?


        def dfs(i):

            # Take
            if isPalin:
                list.append(str[i:j])

            # Skip
            if isPalin:
                dfs() # make it wider?

            i -= 1
            j += 1

        While loop to expand or something??
        Choose to keep expanding or not?
        When to move i up to j?
        if you choose to take the current palin, then gotta move i/j both up?
        1. if [i:j] isPalin, choose to...
            1. use slice
                1. add to result
                2. move i/j up to j + 1 (keep distance? or both on top of each other?)
            2. keep expanding anyways (trying to get a bigger palin)
                1. 
        whether is or isn't a palin, the other option is to expand regardless
 
        all = []
        " r a c e c a r "
          i           
            j

        
        def backtrack(i, currPart):
            if i >= len(s):
                res.append(currPart)
                return
 
            j = i
            while j < len(s):
                if isPalin(s[i:j]):
                    # Use slice
                    currPart.append(s[i:j])
                    backtrack(j + 1, currPart)
                    # Don't use slice and keep looking for other options
                    currPart.pop()?
    
                # Expand
                j += 1
        """
        
        res = []
        def backtrack(i, j, currPart):
            if j >= len(s):
                if i == j:
                    res.append(currPart.copy())
                return
 
            if isPalin(s, i, j):
                # Use slice
                currPart.append(s[i:j + 1])
                backtrack(j + 1, j + 1, currPart)
                # Don't use slice and keep looking for other options
                currPart.pop()

            # Expand
            backtrack(i, j + 1, currPart)

        def isPalin(s, i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        backtrack(0, 0, [])
        return res