class Solution(object):
    def minEatingSpeed(self, arr, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low = 1
        high = max(arr)

        while low <= high:
            mid = (low + high) // 2
            total = self.hours(arr, mid)
            if total <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low            



    def hours(self, arr, mid):
        banana = 0
        for i in range(len(arr)):
            banana += (arr[i] + mid - 1) // mid
        return banana        
        