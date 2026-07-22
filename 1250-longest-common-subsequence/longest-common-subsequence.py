class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        # Space Optimized DP
        m, n = len(text1), len(text2)

        prev = [0] * (n + 1)

        for i in range(m - 1, -1, -1):
            curr = [0] * (n + 1)

            for j in range(n - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(prev[j], curr[j + 1])

            prev = curr

        return prev[0]
        
        # # 1st Solution
        # m, n = len(text1), len(text2)

        # dp = [[0] * (n + 1) for _ in range(m + 1)]

        # for i in range(m - 1, -1, -1):
        #     for j in range(n - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

        # return dp[0][0]
        