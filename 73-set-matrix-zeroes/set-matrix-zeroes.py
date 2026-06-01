class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = [0 for x in matrix]
        cols = [0 for x in matrix[0]]
        for i in range(len(matrix)):
            for j, element in enumerate(matrix[i]):
                if element == 0: 
                    rows[i] = 1
                    cols[j] = 1
        print(rows, cols)
        
        for i in range(len(matrix)):
            for j, element in enumerate(matrix[i]):
                if (matrix[i][j] != 0 and (rows[i] == 1 or cols[j] == 1)):
                    matrix[i][j] = 0




        # m, n = len(matrix), len(matrix[0])

        # first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        # first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # for i in range(1, m):
        #     for j in range(1, n):
        #         if matrix[i][j] == 0:
        #             matrix[i][0] = 0
        #             matrix[0][j] = 0

        # for i in range(1, m):
        #     for j in range(1, n):
        #         if matrix[i][0] == 0 or matrix[0][j] == 0:
        #             matrix[i][j] = 0

        # if first_row_zero:
        #     for j in range(n):
        #         matrix[0][j] = 0

        # if first_col_zero:
        #     for i in range(m):
        #         matrix[i][0] = 0