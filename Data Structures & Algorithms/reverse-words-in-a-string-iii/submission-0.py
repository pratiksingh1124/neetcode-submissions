class Solution:
    def reverseWords(self, s: str) -> str:
        pass #default
        words = s.split(" ") #space characters
        res = []

        for w in words:
            res.append(w[::-1]) #appending in empty list

        return " ".join(res)

