class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        {
            3: "def"
            4: "ghi"
        }
        "34"
        """

        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res, string = [], []
        def backtrack(i):
            if i >= len(digits):
                if len(string):
                    res.append("".join(string))
                return
 
            digit = digits[i]
            charOptions = digitMap[digit]
            for char in charOptions:
                # Take
                string.append(char)
                backtrack(i + 1)

                # Backtrack/Skip
                string.pop()

        backtrack(0)
        return res