class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1    
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1                

        
        
        
        
        
        
        
        
        # n = len(nums)

        # for i in range(n):
        #     if nums[i] == target:
        #         return i
        # return -1
        
        # low = 0
        # high = len(nums) - 1

        # while low <= high:

        #     mid = (low + high) // 2

        #     if nums[mid] == target:
        #         return mid
 
        #     if nums[low] <= nums[mid]:

        #         if nums[low] <= target < nums[mid]:
        #             high = mid - 1
        #         else:
        #             low = mid + 1
        #     else:

        #         if nums[mid] < target <= nums[high]:
        #             low = mid + 1
        #         else:
        #             high = mid - 1

        # return -1