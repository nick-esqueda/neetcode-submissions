class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Can use each candidate AT MOST ONCE - but can use two 2s if there are two 2s in the list
        No duplicates (permutations of same nums)

        Take - must move forward, can't re-use
        Skip - move forward

        [9,2,2,4,6,1,5]

        [1,2,2,4,5,6,9]
             i
        """

        candidates.sort()
        allCombos = []
        def backtrack(i, combo, remaining):
            if remaining == 0:
                allCombos.append(combo.copy())
            if i >= len(candidates) or remaining <= 0:
                return

            # Take - include num dupes
            combo.append(candidates[i])
            backtrack(i + 1, combo, remaining - candidates[i])

            # Skip - scoot i up to exclude num dupes
            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, combo, remaining)
        
        backtrack(0, [], target)
        return allCombos