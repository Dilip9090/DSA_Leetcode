class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def backtrack(path, used):

            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])

                backtrack(path, used)

                path.pop()
                used[i] = False

        backtrack([], [False] * len(nums))

        return ans