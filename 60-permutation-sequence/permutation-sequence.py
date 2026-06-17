class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n + 1)]

        fact = 1
        for i in range(1, n):
            fact *= i

        k -= 1

        ans = []

        while nums:

            idx = k // fact

            ans.append(nums[idx])

            nums.pop(idx)

            if not nums:
                break

            k %= fact
            fact //= len(nums)

        return "".join(ans)