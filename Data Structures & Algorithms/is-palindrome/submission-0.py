class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([c for c in s if c.isalnum()])
        print(s)
 
        l = 0
        r = len(s) - 1
        while l < r:
            lChar = s[l]
            rChar = s[r]

            if lChar != rChar:
                return False
 
            l += 1
            r -= 1
        
        return True