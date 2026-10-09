class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Must move to next idx whether taking or skipping

        []
        [9,2,2,4,6,1,5]
           i
        
        if you've seen the # already, exclude it? since would have found same combos as earlier, right?

        don't want to include another "1" on the same path we decided to skip "1"
        but why wouldn't you want to use the other 1?
        > because it gets the same sum result
        > plus, we already checked & backtracked when including the first 1
        """

        candidates.sort()

        allCombos = []
        def backtrack(i, combo, comboSum):
            if comboSum == target:
                allCombos.append(combo.copy())
            if i >= len(candidates) or comboSum >= target:
                return

            # Take
            combo.append(candidates[i])
            backtrack(i + 1, combo, comboSum + candidates[i])

            # Skip
            combo.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, combo, comboSum)

        backtrack(0, [], 0)
        return allCombos
 