class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        ans = 0

        for num in nums:

            if num == 1:
                count += 1
                ans = max(ans, count)

            else:
                count = 0

        return ans