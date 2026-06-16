class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        ans = []

        def backtrack(idx, subset):

            ans.append(subset[:])

            for i in range(idx, len(nums)):

                if i > idx and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])

                backtrack(i + 1, subset)

                subset.pop()

        backtrack(0, [])

        return ans
        