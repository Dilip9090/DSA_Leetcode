class Robot:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0
        self.cycle = 2 * (self.w + self.h - 2)

    def step(self, num):
        num %= self.cycle

        if num == 0:
            if self.x == 0 and self.y == 0:
                self.dir = 3
            return

        while num > 0:
            if self.dir == 0:
                if self.x + 1 < self.w:
                    self.x += 1
                else:
                    self.dir = 1
                    self.y += 1

            elif self.dir == 1:
                if self.y + 1 < self.h:
                    self.y += 1
                else:
                    self.dir = 2
                    self.x -= 1

            elif self.dir == 2:
                if self.x - 1 >= 0:
                    self.x -= 1
                else:
                    self.dir = 3
                    self.y -= 1

            else:
                if self.y - 1 >= 0:
                    self.y -= 1
                else:
                    self.dir = 0
                    self.x += 1

            num -= 1

    def getPos(self):
        return [self.x, self.y]

    def getDir(self):
        return ["East", "North", "West", "South"][self.dir]