class Solution(object):
    def lengthOfLongestSubstring(self, s):


        n = len(s)
        if n<=1:
            return n

        set1 = set({})

        i,j = 0,1

        set1.add(s[0])
        ans = 1

        while j<n:
            while s[j] in set1:
                set1.discard(s[i])
                i+=1

            set1.add(s[j])
            j+=1
            ans = max(ans,(j-i)) 

        return ans       

        """
        :type s: str
        :rtype: int
        """
        