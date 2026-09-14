class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        intuition: permutation, so thinking count map

        maintain freq counter for static sliding window
        on each iter, check if window freq count matches other string counter
        """

        s1Counter = [0] * 26
        s2Counter = [0] * 26

        # Initialize s1Counter
        for c in s1:
            s1Counter[ord(c) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            # Initialize first few chars of window
            if r < len(s1) - 1:
                s2Counter[ord(s2[r]) - ord('a')] += 1
                continue

            s2Counter[ord(s2[r]) - ord('a')] += 1

            # Compare counters
            if s1Counter == s2Counter:
                return True

            s2Counter[ord(s2[l]) - ord('a')] -= 1
            l += 1

        return False
 