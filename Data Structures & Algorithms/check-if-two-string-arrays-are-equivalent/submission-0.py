class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        pass
        s1 = ""
        s2 = ""

        for w in word1:
            s1 += w #add words in word1

        for w in word2:
            s2 += w  #add words in word2

        return s1 == s2 #T OR F

