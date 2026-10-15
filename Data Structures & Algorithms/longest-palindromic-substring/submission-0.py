class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        basically need to find/compare all palins and return the longest one
        or, keep a running var holding the longest as you go

        could have digits
        could have lower and upper english
        is palindrome case-sensitive?

        iter forward and go outwards, updating as you go along?

        longest = bab
        "ababd"
           i
             j
        
        always do bounds check
        """

        longest = (0, 0)

        # Odd lengths
        for i, c in enumerate(s):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) >= (longest[1] - longest[0]):
                    longest = (l, r)
                l -= 1
                r += 1
        
        # Even lengths
        for i, c in enumerate(s):
            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) >= (longest[1] - longest[0]):
                    longest = (l, r)
                l -= 1
                r += 1


        return s[longest[0]:longest[1]+1]