class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #set a variable to check later

        for num in nums: #defined earlier in the function
            if num in seen:
                return True

            seen.add(num)

        return False