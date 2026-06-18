class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + c // 3].add(num)

        def backtrack(idx):
            if idx == len(empty):
                return True

            r, c = empty[idx]
            box = (r // 3) * 3 + c // 3

            for num in "123456789":
                if (num not in rows[r] and
                    num not in cols[c] and
                    num not in boxes[box]):

                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)

                    if backtrack(idx + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box].remove(num)

            return False

        backtrack(0)



        
        # def isValid(row, col, num):

        #     for i in range(9):

        #         if board[row][i] == num:
        #             return False

        #         if board[i][col] == num:
        #             return False

        #     startRow = (row // 3) * 3
        #     startCol = (col // 3) * 3

        #     for i in range(3):
        #         for j in range(3):

        #             if board[startRow + i][startCol + j] == num:
        #                 return False

        #     return True

        # def solve():

        #     for row in range(9):
        #         for col in range(9):

        #             if board[row][col] == ".":

        #                 for num in "123456789":

        #                     if isValid(row, col, num):

        #                         board[row][col] = num

        #                         if solve():
        #                             return True

        #                         board[row][col] = "."

        #                 return False

        #     return True

        # solve()
        