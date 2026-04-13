class Solution(object):
    def getMinDistance(self, nums, target, start):
        min_dist = float('inf')
        
        for i in range(len(nums)):
            if nums[i] == target:
                dist = abs(i - start)
                min_dist = min(min_dist, dist)
        
        return min_dist


        # elif (nums[k]) == target:
        #     return nums[k] - start
        #     k += 1
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        