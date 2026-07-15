class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n
        ##Brute force 
        # sumOdd = 0
        # odd = 1

        # for _ in range(n):
        #     sumOdd += odd
        #     odd += 2

        # sumEven = 0
        # even = 2

        # for _ in range(n):
        #     sumEven += even
        #     even += 2

        # while sumEven:
        #     sumOdd, sumEven = sumEven, sumOdd % sumEven

        # return sumOdd