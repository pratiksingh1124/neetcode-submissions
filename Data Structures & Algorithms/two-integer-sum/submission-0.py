class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # empty dictionary
        for i in range(len(nums)):
            num = nums[i]
            needed = target - num

            if needed in seen: # stores value of the first number if the 
                return [seen[needed], i] # condition is not satisfied via seen[]

            seen[num] = i




        # for i, num in enumerate(nums):
        #     needed = target - num

        #     if needed in seen:
        #         return [seen[needed], i]

        #     seen[num] = i 


    #   for i, num in seperate(nums):
    #       needed = target - num

    #       if needed in seen:
    #          return
           # seen
 



         