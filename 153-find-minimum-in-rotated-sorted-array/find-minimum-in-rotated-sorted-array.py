class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        ans = float('inf')

        while low <= high:
            mid = (low + high) // 2
            if nums[low] <= nums[high]:
                ans = min(ans,nums[low])
                break
            if nums[mid] <= nums[high]:
                high = mid - 1
                ans = min(ans, nums[mid])
            else:
                low = mid + 1
                ans = min(ans, nums[low])
        return ans            