class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Track which places are ones.
        Use new integers (1 per iteration) to track the 1s (shift to correct position, 32 - i)
        OR the integers together to get the final number

        00000000000000000000000000010101 - 1
        00000000000000000000000000001010 - 0
        00000000000000000000000000000101 - 1
        00000000000000000000000000000010 - 0
        00000000000000000000000000000001 - 1
        00000000000000000000000000000000 - 0

        10000000000000000000000000000000 - 1
        00000000000000000000000000000000 - 0
        00100000000000000000000000000000 - 1
        00000000000000000000000000000000 - 0
        00001000000000000000000000000000 - 1
        """
        result = 0
        for i in range(32):
            one = n & 1                   # 0b1 or 0b0
            placeholder = one << (31 - i) # Shift to the mirrored position
            result |= placeholder         # OR together with result to "add" the new bit
            n >>= 1                       # Shift n to get the next digit
        return result
