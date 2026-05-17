class Solution:
    def rotate(self, arr, k):

        n = len(arr)

        k = k % n

        arr.reverse()

        arr[:k] = reversed(arr[:k])

        arr[k:] = reversed(arr[k:])