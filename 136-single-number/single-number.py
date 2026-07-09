class Solution(object):
    def singleNumber(self, nums):
        #More Batter 
        mpp = {}

        for i in nums:
            if i in mpp:
                mpp[i] += 1
            else:
                mpp[i] = 1

        for key in mpp:
            if mpp[key] == 1:
                return key            




        # # Batter Solution
        # maxi = max(nums)
        # uni = [0] * (maxi + 1)
        # n = len(nums)

        # for i in nums:
        #     uni[i] += 1

        # for i in range(len(uni)):
        #     if uni[i] == 1:
        #         return i    

        
        
        
        
        
        
        
        # Brute Force
        # n = len(nums)

        # for i in range(n):
        #     noo = nums[i]
        #     count = 0
        #     for k in range(n):
        #         if nums[k] == noo:
        #             count += 1
        #     if count == 1:
        #         return nums[i]



        # opop = []
        # for x in nums:
        #     if x in opop:
        #         opop.remove(x)
        #     else:
        #         opop.append(x)
        # return opop[0]

