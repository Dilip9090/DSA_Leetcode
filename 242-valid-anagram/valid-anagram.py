class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

# s ="ajhagskjdfhsj"
# t ="jhagskjdfhsjk"
#         a = s[1:]
#         b = t[0:]
#         r = True
#         w = False

#         if a != b:
#             return False

#         if a == b:
#             return True        
#         # if a == b:
#         #     print ("True")
#         # else:
#         #     True
# # # print(a)
# #     while a == b:
# #         print(r)
# #         break
# #     else:
# #         print(w)

        