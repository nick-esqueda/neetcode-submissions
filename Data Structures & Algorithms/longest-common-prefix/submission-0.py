class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = float('inf')
        for s in strs:
            smallest = min(smallest, len(s))

        longest = ""
        for i in range(smallest):
            chars = set()
            for s in strs:
                chars.add(s[i])
            
            if len(chars) > 1:
                break
            longest += list(chars)[0]

        return longest
