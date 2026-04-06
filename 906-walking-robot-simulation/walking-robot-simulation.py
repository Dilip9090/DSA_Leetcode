class Solution(object):
    def robotSim(self, commands, obstacles):
        # Directions: North, East, South, West
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0  # start facing north
        
        x = y = 0
        obstacle_set = set(map(tuple, obstacles))
        
        max_dist = 0
        
        for cmd in commands:
            if cmd == -1:  # turn right
                d = (d + 1) % 4
            elif cmd == -2:  # turn left
                d = (d - 1) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    if (x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        