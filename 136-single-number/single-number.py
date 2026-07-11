class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mapp = {}

        for i in nums:
            if i in mapp:
                mapp[i] += 1
            else:
                mapp[i] = 1
        for key in mapp:
            if mapp[key] == 1:
                return key            



        # #2. Solution 
        # maxi = max(nums)
        # uni = [0] * (maxi + 2)
        # n = len(nums)

        # for i in nums:
        #     uni[i] += 1

        # for j in range(len(uni)):
        #     if uni[j] == 1:
        #         return j    


        ## 1. Solution
        # arr = []

        # for i in nums:
        #     if i in arr:
        #         arr.remove(i)
        #     else:
        #         arr.append(i)
        # return arr[0]                