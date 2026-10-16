class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != char:
                    return longest
            longest += char
        return longest
