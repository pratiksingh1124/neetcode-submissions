class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sorted_word = sorted(word)
            key = "" #initially empty

            for char in sorted_word:
                key += char #adding characters

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        answer = []

        for group in groups:
            answer.append(groups[group])

        return answer


        # groups = {}

        # for word in strs:
        #     key = ''.join(sorted(word))

        #     if key not in groups:
        #         groups[key] = []

        #     groups[key].append(word)

        # return list(groups.values())