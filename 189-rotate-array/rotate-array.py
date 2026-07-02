class Solution:
    def rotate(self, arr, k):
        n = len(arr)
        k = k % n
        temp = []
        l = 0
        p = 0

        for i in range(0,n-k):
            temp.append(arr[i])

        for s in range(n-k,n):
            arr[l] = arr[s]
            l += 1

        for t in range(k,n):
            arr[t] = temp[p]
            p += 1
        return arr            
            




        # n = len(arr)

        # k = k % n

        # arr.reverse()

        # arr[:k] = reversed(arr[:k])

        # arr[k:] = reversed(arr[k:])