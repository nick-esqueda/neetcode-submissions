class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        What if this one went here? Or this one? Or this one?...
        [_, _, _]
        Can only use a candidate once
        """

        allPerms = []
        def backtrack(perm, remaining):
            if not remaining:
                allPerms.append(perm.copy())
                return

            for num in nums:
                if num not in remaining:
                    continue

                perm.append(num)
                remaining.remove(num)
                backtrack(perm, remaining)

                remaining.add(num)
                perm.pop()

        backtrack([], set(nums))
        return allPerms
        