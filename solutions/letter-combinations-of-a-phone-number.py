class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charmap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if digits == "": return ""
        output = [x for x in charmap[digits[0]]]
        for i in list(digits)[1:]:
            output = [list(output) for x in range(len(charmap[i]))]
            for j in range(len(output)):
                for k in range(len(output[j])):
                    output[j][k] += charmap[i][j]
            output = list(chain.from_iterable(output))
        return output
