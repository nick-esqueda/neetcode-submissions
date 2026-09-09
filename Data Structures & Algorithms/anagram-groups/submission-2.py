from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # SOLUTION: Encode strings into char count strings and put the original string with it's corresponding map key
 
        def createCountKey(s: str) -> list:
            countList = [0] * 26
            for char in s:
                charIdx = ord(char) - 97
                countList[charIdx] += 1
            return tuple(countList)

        anagramGroups = defaultdict(list)

        for s in strs:
            key = createCountKey(s)
            anagramGroups[key].append(s)

        result = []
        for key in anagramGroups:
            result.append(anagramGroups[key])
 
        return result