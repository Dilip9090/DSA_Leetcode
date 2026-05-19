class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        # seen = {}
        
        # for i, num in enumerate(nums):
        #     complement = target - num
            
        #     if complement in seen:
        #         return [seen[complement], i]
        #     seen[num] = i




        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        