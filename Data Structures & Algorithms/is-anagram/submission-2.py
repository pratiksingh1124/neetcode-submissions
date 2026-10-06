class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False #if length is not same, the pair is obviously denied
        for char in set(s):
            count1 = s.count(char)
            count2 = t.count(char)
            if count1 != count2: #check for each unique character
                return False
        return True
# use of dictionary makes it more efficient...
# since we don't have to count again and again like the first case 