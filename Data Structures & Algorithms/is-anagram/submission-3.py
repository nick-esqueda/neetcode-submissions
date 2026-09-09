class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # SOLUTION: Use array[26] to maintain alphabet counts

        # Return False early if string lengths don't match - impossible to be an anagram
        if len(s) != len(t):
            return False

        counts = [0] * 26

        # For each char in both strings, increment/decrement the associated counts index
        for i in range(len(s)):
            sIdx = ord(s[i]) - 97
            tIdx = ord(t[i]) - 97
            counts[sIdx] += 1 # Increment for S chars
            counts[tIdx] -= 1 # Decrement for T chars
        
        # Check if any count is NOT zero - if so, then the strings are not equal/not anagrams
        for count in counts:
            if count != 0:
                return False

        # If all counts were zero, then the string is an anagram
        return True


