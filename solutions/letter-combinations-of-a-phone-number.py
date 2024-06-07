class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charmap = [
            (),
            (),
            ("a","b","c"),
            ("d","e","f"),
            ("g","h","i"),
            ("j","k","l"),
            ("m","n","o"),
            ("p","q","r","s"),
            ("t","u","v"),
            ("w","x","y","z")
        ]
        if digits == "": return ""
        output = [x for x in charmap[int(digits[0])]]
        for i in list(digits)[1:]:
            output = [list(output) for x in range(len(charmap[int(i)]))]
            for j in range(len(output)):
                for k in range(len(output[j])):
                    output[j][k] += charmap[int(i)][j]
            output = list(chain.from_iterable(output))
        return output
