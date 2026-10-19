class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            res.append((digits[i] + carry) % 10) # num, or 0 when sum is 10
            carry = (digits[i] + carry) // 10    # 0 when sum < 10, 1 when 10
        if carry:
            res.append(1)

        res.reverse()
        return res
