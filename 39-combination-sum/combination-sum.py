class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        def backtrack(idx, target, curr):

            if target == 0:
                ans.append(curr[:])
                return

            if idx == len(candidates) or target < 0:
                return

            curr.append(candidates[idx])
            backtrack(idx, target - candidates[idx], curr)
            curr.pop()

            backtrack(idx + 1, target, curr)

        backtrack(0, target, [])

        return ans