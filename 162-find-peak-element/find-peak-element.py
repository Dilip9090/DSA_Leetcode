class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = -1

        if n == 1:
            return 0

        for i in range(n):
            if i == 0 and nums[0] > nums[1]:
                ans = 0
            elif i == n - 1 and nums[n - 1] > nums[n - 2]:
                ans = n - 1    
            elif nums[i] > nums[i - 1] and nums[i] > nums[i + 1] and nums[i] > nums[ans]:
                ans = i
        return ans            
