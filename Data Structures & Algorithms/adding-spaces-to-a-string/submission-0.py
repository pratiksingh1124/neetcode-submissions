class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        pass
        res = "" #empty to be updated
        j = 0

        for i in range(len(s)): #complete length of characters
            if j < len(spaces) and i == spaces[j]: #run only till 0<number of spaces
                res += " " #actual space
                j += 1

            res += s[i] #accesses a character

        return res


