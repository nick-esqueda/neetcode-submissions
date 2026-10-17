class Solution:
    def hammingWeight(self, n: int) -> int:
        numBits = 0
        while n:
            if n & 1 == 1:
                numBits += 1
            n >>= 1
        return numBits
