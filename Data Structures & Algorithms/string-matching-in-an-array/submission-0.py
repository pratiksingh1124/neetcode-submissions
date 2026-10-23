class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for w in words:
            for s in words:
                if w != s and w in s:
                    res.append(w)
                    break

        return res
