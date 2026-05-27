class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lower = set()
        upper = set()

        for ch in word:
            if 'a' <= ch <= 'z':
                lower.add(ch)
            else:
                upper.add(ch.lower())

        return len(lower.intersection(upper))
        