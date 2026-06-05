class Solution(object):
    def myPow(self, x, n):

        N = n

        if N < 0:
            x = 1 / x
            N = -N

        ans = 1

        while N:
            if N % 2 == 1:
                ans *= x

            x *= x
            N //= 2

        return ans
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        