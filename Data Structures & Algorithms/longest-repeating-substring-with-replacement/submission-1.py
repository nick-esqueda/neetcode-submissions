from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        the max consecutive chars are important

        "i can tolerate K being different within the substring"

        windowMap = {
            a: 2
            b: 0
            x: 1
            y: 1
        }
        lenWindow - maxChar <= k
        lenWindow = r - l + 1
        """
        if len(s) <= 1:
            return len(s)
        
        freq = [0] * 26 # freq[ord('B') - ord('A')] = 8
        maxLength = 0
        l = 0
        for r, c in enumerate(s):
            # Increment the window frequency counter
            freq[ord(c) - ord("A")] += 1

            # Find the count of the most frequent char in the window
            maxCharCount = max(freq)

            # Calculate window length
            windowLength = r - l + 1

            # Move L up until the window is valid if needed
            while windowLength - maxCharCount > k:
                freq[ord(s[l]) - ord("A")] -= 1
                l += 1
                windowLength -= 1
                maxCharCount = max(freq)

            # Update max
            maxLength = max(maxLength, windowLength)

        return maxLength
