class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        "a b c d c e f"
               l
                     r
        set({ d, c, e, f })
        len = 4
        """
        
        windowSet = set()
        maxLength = 0
        l = 0
        for r in range(len(s)):
            # Move L up, removing chars from the window set, until the R char is out.
            while s[r] in windowSet:
                windowSet.remove(s[l])
                l += 1

            # Add the new char to the window set
            windowSet.add(s[r])
 
            # Update max length
            length = r - l + 1
            maxLength = max(maxLength, length)

        return maxLength