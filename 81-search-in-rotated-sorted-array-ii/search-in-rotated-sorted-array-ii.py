class Solution(object):
    def search(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(arr)
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return True
            elif arr[low] == arr[mid] and arr[mid] == arr[high]:
                low += 1
                high -= 1 
                continue   
            if arr[low] <= arr[mid]: 
                if arr[low] <= target and target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if arr[mid] < target and target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False            
