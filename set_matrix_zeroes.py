class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    self.set_zero(matrix, row, col)
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 'a' or matrix[row][col] == 0:
                    matrix[row][col] = 0
                    
    
    def set_zero(self, matrix, row, col):
        # given a row and column, set everything to -1.
        for i in range(len(matrix)):
            if matrix[i][col] != 0:
                matrix[i][col] = 'a'
        for i in range(len(matrix[row])):
            if matrix[row][i] != 0:
                matrix[row][i] = 'a'
