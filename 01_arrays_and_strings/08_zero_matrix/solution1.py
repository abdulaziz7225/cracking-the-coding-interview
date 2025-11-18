from typing import List


# Solution 1: With additional data structure
class Solution:
    def zero_matrix(self, matrix: List[List[int]]) -> None:
        row_len = len(matrix)
        col_len = len(matrix[0])

        row_zeros = [False] * row_len
        col_zeros = [False] * col_len

        for row_idx in range(row_len):
            for col_idx in range(col_len):
                if matrix[row_idx][col_idx] == 0:
                    row_zeros[row_idx] = True
                    col_zeros[col_idx] = True

        for row_idx in range(row_len):
            for col_idx in range(col_len):
                if row_zeros[row_idx] or col_zeros[col_idx]:
                    matrix[row_idx][col_idx] = 0

# m = row length, n = column length
# Time Complexity: O(2 * m * n + m + n) ==> O(m * n)
# Space Complexity: O(m + n)


class TestZeroMatrix:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_3_by_3(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        self.s.zero_matrix(matrix)
        assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    def test_4_by_4(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        self.s.zero_matrix(matrix)
        assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    def test_3_by_5(self):
        matrix = [[-4, -2147, 6, -7, 0],
                  [-8, 6, -8, -6, 0], [2147, 2, -9, -6, -10]]
        self.s.zero_matrix(matrix)
        assert matrix == [[0, 0, 0, 0, 0], [
            0, 0, 0, 0, 0], [2147, 2, -9, -6, 0]]
