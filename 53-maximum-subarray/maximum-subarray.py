class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        ans = nums[0]
        cur_sum = 0
        for i in nums:
            cur_sum+=i
            if cur_sum>ans:
                ans = cur_sum
            if cur_sum<0:
                cur_sum=0

        return ans               





        """
        :type nums: List[int]
        :rtype: int
        """
        