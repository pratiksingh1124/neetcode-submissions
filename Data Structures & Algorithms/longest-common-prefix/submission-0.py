class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in strs:
            while not s.startswith(prefix):
                prefix = prefix[:-1] #slice and give everything except the last chr

        return prefix
