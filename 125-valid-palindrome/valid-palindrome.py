class Solution(object):
    def isPalindrome(self, s):
        clean = ""

        for ap in s:
            if ap.isalnum():
                clean += ap.lower()
        if clean == clean[::-1]:
            return True
        return False  





        # s = s.replace(" ","")
        # s = s.replace(",","")
        # s = s.replace(":","")
        # s = s.replace(".", "")
        # s = s.replace(":", "")
        # s = s.replace("/", "")
        # s = s.replace("?", "")
        # s = s.replace("@", "")
        # s = s.replace("#", "")
        # s = s.replace("$", "")
        # s = s.replace("_", "")
        # s = s.replace("[", "")
        # s = s.replace("]", "")
        # s = s.replace("(", "")
        # s = s.replace(")", "")
        # s = s.replace("{", "")
        # s = s.replace("}", "")
        # s = s.replace(".", "")
        # s = s.replace("|", "")
        # s = s.replace(""""\"""" , """ """)
        # s = s.lower()
        # if s == s[::-1]:
        #     return True
        # return False    
        
        """
        :type s: str
        :rtype: bool
        """
        