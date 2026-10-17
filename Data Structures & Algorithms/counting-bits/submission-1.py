class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            count = 0
            for j in range(32):
                andedResult = i & (1 << j)
                if andedResult:
                    count += 1
            result.append(count)
        return result