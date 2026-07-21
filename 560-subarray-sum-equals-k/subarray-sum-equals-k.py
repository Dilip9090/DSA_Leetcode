class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        presum = [0] * n
        presum[0] = nums[0]
        mpp = {0: 1}
        count = 0

        for i in range(1, n):
            presum[i] = presum[i - 1] + nums[i]

        for j in range(n):
            val = presum[j] - k
            if val in mpp:
                count += mpp[val]
            if presum[j] in mpp:
                mpp[presum[j]] += 1
            else:
                mpp[presum[j]] = 1
        return count

        # n = len(nums)
        # count = 0

        # for i in range (n):
        #     sum1 = 0
        #     for j in range(i,n):
        #         sum1 += nums[j]
        #         if sum1 == k:
        #             count += 1
        # return count
