class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        which one goes in this spot?
        any one of them could go in each spot.
        so, choose one, iter forward, choose another from remaining

        have to mark which are remaining/usable and unusable


        [1, 2, 3]
        {1, 3}
        [2, 1, _]

        choose each of the remaining options in for loop
        """
        allPerms = []
        def buildPermutations(perm, remaining):
            if not remaining:
                allPerms.append(perm.copy())
                return

            for num in nums:
                if num not in remaining:
                    continue

                # Use this num
                perm.append(num)
                remaining.remove(num)
 
                buildPermutations(perm, remaining)
 
                # Remove this num
                perm.pop()
                remaining.add(num)

        buildPermutations([], set(nums))
        return allPerms
        