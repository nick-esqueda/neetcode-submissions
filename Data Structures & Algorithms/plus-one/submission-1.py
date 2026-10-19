class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits

        res = [-1] * len(digits)
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if not carry:
                res[i] = digits[i]
            else:
                sm = digits[i] + 1
                if sm == 10:
                    res[i] = 0
                    carry = 1
                else:
                    res[i] = sm
                    carry = 0
        
        if carry:
            res = [1] + res
        return res

