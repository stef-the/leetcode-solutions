class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        a=sentence.split(' ')
        for s,i in enumerate(a):
            m=100
            for j in dictionary:
                if i[:len(j)]==j and m>len(j):
                    a[s]=j
                    m=len(j)
        return " ".join(a)
