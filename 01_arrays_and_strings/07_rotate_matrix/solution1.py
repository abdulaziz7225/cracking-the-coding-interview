from typing import List


class Solution:
    def rotate_matrix(self, matrix: List[List]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Swapping entire rows doesn’t change complexity (each swap is O(1) because it's a list reference swap).
# Time Complexity: O(n^2 + n) ==> O(n^2)
# Space Complexity: O(1)


class TestRotateImage:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_with_3_by_3_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.s.rotate_matrix(matrix)
        assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    def test_with_4_by_4_matrix(self):
        matrix = [[5, 1, 9, 11], [2, 4, 8, 10],
                  [13, 3, 6, 7], [15, 14, 12, 16]]
        self.s.rotate_matrix(matrix)
        assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1],
                          [12, 6, 8, 9], [16, 7, 10, 11]]
