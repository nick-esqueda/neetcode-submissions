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
        freq = [0] * 26
        maxLength = 0
        l = 0
        for r, c in enumerate(s):
            # Increment the window frequency counter
            freq[ord(c) - ord("A")] += 1

            # Move L up until the window is valid if needed
            # Valid = The size of the window - the count of the most frequent char in the window <= k 
            while (r - l + 1) - max(freq) > k:
                freq[ord(s[l]) - ord("A")] -= 1
                l += 1

            # Update max
            maxLength = max(maxLength, (r - l + 1))

        return maxLength
