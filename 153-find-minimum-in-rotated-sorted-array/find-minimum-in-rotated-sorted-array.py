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
            if nums[mid] <= nums[high]:
                high = mid - 1
                if ans > nums[mid]:
                    ans = nums[mid]
            else:
                low = mid + 1
                if ans > nums[mid]:
                    ans = nums[mid]
        return ans            