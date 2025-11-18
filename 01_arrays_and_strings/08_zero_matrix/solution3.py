from typing import List


# Solution 3: In-place operation with one flag
class Solution:
    def zero_matrix(self, matrix: List[List[int]]) -> None:
        row_len = len(matrix)
        col_len = len(matrix[0])

        first_col_has_zero = False

        for row_idx in range(row_len):
            if matrix[row_idx][0] == 0:
                first_col_has_zero = True

            for col_idx in range(1, col_len):
                if matrix[row_idx][col_idx] == 0:
                    matrix[row_idx][0] = 0
                    matrix[0][col_idx] = 0

        for row_idx in range(row_len - 1, -1, -1):
            for col_idx in range(1, col_len):
                if matrix[row_idx][0] == 0 or matrix[0][col_idx] == 0:
                    matrix[row_idx][col_idx] = 0
            if first_col_has_zero:
                matrix[row_idx][0] = 0

# m = row length, n = column length
# Time Complexity: O(2 * m * n) ==> O(m * n)
# Space Complexity: O(1)


class TestZeroMatrix:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_3_by_3(self):
        matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        self.s.zero_matrix(matrix)
        assert matrix == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_4_by_4(self):
        matrix = [[1, 2, 0, 4], [5, 6, 7, 8], [9, 10, 11, 0], [13, 14, 15, 0]]
        self.s.zero_matrix(matrix)
        assert matrix == [[0, 0, 0, 0], [
            5, 6, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def test_3_by_5(self):
        matrix = [[6, 1, 0, 2, 9], [1, 7, 4, 3, 5], [8, 3, 7, 0, 5]]
        self.s.zero_matrix(matrix)
        assert matrix == [[0, 0, 0, 0, 0], [1, 7, 0, 0, 5], [0, 0, 0, 0, 0]]
