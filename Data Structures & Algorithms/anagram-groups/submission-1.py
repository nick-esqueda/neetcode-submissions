from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # (MAYBE NOT?) Subproblem: Determine if a string is an anagram
        
        # How to group anagrams together in a list?
        # Map of each string to know char counts and compare map?
        # encode string "key" that says what the group is for? would need to make sure it's alphabetical though
        #   { "a1c1r1": ["car", "rac"] }
        # Use a count array[26], then stringify that to use as the map key to categorize anagrams
        #   { "101000...010....0": ["car", "rac"] }
        # sort each string?


        # For each string, create an array[26] char counter (will be used as map key)
        # Put that string in the map based on it's map key
        # defaultdict list

        def createCountKey(s: str) -> list:
            countList = [0] * 26
            for char in s:
                charIdx = ord(char) - 97
                countList[charIdx] += 1
            return str(countList)

        anagramGroups = defaultdict(list)

        for s in strs:
            key = createCountKey(s)
            anagramGroups[key].append(s)

        result = []
        for key in anagramGroups:
            result.append(anagramGroups[key])
 
        return result