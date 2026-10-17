class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        00001010
        00000100 &
            0100
        
        AND by the places/powers of 2
        if the result is 0, then the OG number has a 0 in that place
        """
        maxInt = 2**32
        mask = 1
        count = 0

        while mask <= maxInt:
            result = n & mask
            if result != 0:
                count += 1
            mask *= 2
        return count
        