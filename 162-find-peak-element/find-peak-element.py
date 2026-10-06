class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 1:
            return 0  
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return (n - 1)        

        low = 1
        high = n - 2

        # if low == 0:
        #     if nums[low] > nums[low + 1]:
        #         return low
        #     low += 1
        # elif high == n - 1:
        #     if nums[high] > nums[high - 1]:
        #         return high
        #     high -= 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid + 1]:
                high = mid - 1
            else:
                low = mid + 1                              
        
        
        
        
        
        
        # n = len(nums)
        # ans = -1

        # if n == 1:
        #     return 0

        # for i in range(n):
        #     if i == 0 and nums[0] > nums[1]:
        #         ans = 0
        #     elif i == n - 1 and nums[n - 1] > nums[n - 2]:
        #         ans = n - 1    
        #     elif nums[i] > nums[i - 1] and nums[i] > nums[i + 1] and nums[i] > nums[ans]:
        #         ans = i
        # return ans            
