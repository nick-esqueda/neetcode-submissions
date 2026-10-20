class Solution:
    """
    "a!f#2n", "j$ad()j$"
    "6#a!f#2n8#j$ad()j$"
     ij
    """

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while j < len(s):
            if s[j] == "#":
                strLen = int(s[i:j])
                strStart, strEnd = j + 1, j + strLen + 1
                res.append(s[strStart:strEnd])
                j, i = strEnd, strEnd
            j += 1
        return res
