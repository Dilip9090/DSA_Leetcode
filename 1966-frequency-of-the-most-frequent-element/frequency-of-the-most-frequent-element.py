class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        
        left = 0
        total = 0
        res = 1
        
        for right in range(len(nums)):
            total += nums[right]
            
            # window invalid ho gaya
            while (right - left + 1) * nums[right] > total + k:
                total -= nums[left]
                left += 1
            
            res = max(res, right - left + 1)
        
        return res






        # #Brute + Hashing (O(n²))
        # nums.sort()
        # n = len(nums)
        # res = 1
        
        # for i in range(n):
        #     target = nums[i]
        #     total_ops = 0
        #     count = 1


        #     for j in range(i-1, -1, -1):
        #         total_ops += target - nums[j]
                
        #         if total_ops > k:
        #             break
                
        #         count += 1
            
        #     res = max(res, count)
        
        # return res