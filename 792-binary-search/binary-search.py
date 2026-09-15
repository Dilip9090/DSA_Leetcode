class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search2(nums, 0, len(nums) - 1, target)

    def search2(self, nums, low, high, target):
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            return self.search2(nums, mid + 1, high, target)
        else:
            return self.search2(nums, low, mid - 1, target)        

        
        # n = len(nums)
        # low = 0
        # high = n - 1

        # while low <= high:
        #     mid = (low + high) // 2

        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] <= target:
        #         low = mid + 1
        #     else:
        #         high = mid - 1 
        # return -1               