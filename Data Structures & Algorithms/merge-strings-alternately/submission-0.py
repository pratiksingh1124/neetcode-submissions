class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        i = 0

        while i < len(word1) and i < len(word2): #till both have equal num of char
            res += word1[i] #adding alternately
            res += word2[i]
            i += 1

        res += word1[i:] #runs if the strings have diff nums of char, prints all  
        res += word2[i:] #remaining charcaters

        return res
