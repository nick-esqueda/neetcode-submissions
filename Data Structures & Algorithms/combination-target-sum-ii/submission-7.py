class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        allCombos = []
        def backtrack(start, combo, remaining):
            if not remaining:
                allCombos.append(combo.copy())
            if start >= len(candidates) or remaining <= 0:
                return

            for i in range(start, len(candidates)):
                if i > 0 and i > start and candidates[i] == candidates[i - 1]:
                    continue
                combo.append(candidates[i])
                backtrack(i + 1, combo, remaining - candidates[i])
                combo.pop()

        backtrack(0, [], target)
        return allCombos