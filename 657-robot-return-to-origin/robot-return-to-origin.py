class Solution(object):
    def judgeCircle(self, moves):

        x , y = 0, 0
        
        for mov in moves:
            if mov == 'U':
                x += 1
            elif mov == 'D':
                x -= 1
            elif mov == 'L':
                y += 1
            elif mov == 'R':
                y -= 1

        return x==0 and y==0
                    



        """

        :type moves: str
        :rtype: bool
        """
        