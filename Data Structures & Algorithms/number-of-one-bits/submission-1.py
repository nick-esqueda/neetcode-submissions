class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        00001010
        00000100 &
            0100
        
        AND by the places/powers of 2
        if the result is 0, then the OG number has a 0 in that place
        """
        count = 0
        for i in range(32):
            andOutput = n & (1 << i)
            if andOutput != 0:
                count += 1
        return count
        