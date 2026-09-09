from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # build a map of chars & counts
        # go through other string to see counts match up

        # Return early if strings aren't the same length - impossible to be an anagram
        if len(s) != len(t):
            return False

        sMap = defaultdict(int)
        tMap = defaultdict(int)

        # Build the map of "char: count" for S and T
        for i in range(len(s)):
            sMap[s[i]] += 1
            tMap[t[i]] += 1

        # Compare the two maps to see if they are equal
        # for sKey, sVal in sMap.items():
        #     tVal = tMap[sKey]
        #     if sVal != tVal:
        #         return False
        # return True

        return sMap == tMap