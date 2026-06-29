class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        start = 0
        maxLen = 1

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):

            l1, r1 = expand(i, i)

            if r1 - l1 + 1 > maxLen:
                start = l1
                maxLen = r1 - l1 + 1

            l2, r2 = expand(i, i + 1)

            if r2 - l2 + 1 > maxLen:
                start = l2
                maxLen = r2 - l2 + 1

        return s[start:start + maxLen]