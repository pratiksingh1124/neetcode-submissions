class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 # index required later

        for char in t:
            if i < len(s) and s[i] == char:
                i += 1 #runs only when the character of index in s
                # is actually eq to the char in t

        return i == len(s) #boolean should be True if characters are subsequent