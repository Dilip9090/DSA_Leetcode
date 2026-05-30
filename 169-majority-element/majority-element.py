class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) // 2]
        # n= len(nums)
        # maxi = 0
        # count = 0

        # for i in range (n):
        #     if nums[i] == maxi :
        #         count += 1
        #         if count <= n/2:
        #             return nums[i]
        #     elif nums[i] != maxi:
        #         maxi = nums[i]


        