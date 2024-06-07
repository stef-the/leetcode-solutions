class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charmap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits: return
        output = []

        def backtrack(n, c):
            if not n:
                return output.append(c)
            [backtrack(n[1:], c + letter) for letter in charmap[n[0]]]

        backtrack(digits, "")
        return output
