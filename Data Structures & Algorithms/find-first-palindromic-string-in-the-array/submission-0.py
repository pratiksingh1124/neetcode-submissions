class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        pass
        for w in words:
            if w == w[::-1]:
                return w
        return ""
