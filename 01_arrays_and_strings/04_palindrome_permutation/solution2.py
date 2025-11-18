# Solution 2: Using bit vector
class Solution:
    def palindrome_permutation(self, string: str) -> bool:
        bit_vector = 0

        for char in string:
            if char.isalpha():
                char = char.lower()
                bit_vector ^= 1 << (ord(char) - ord("a"))

        return bit_vector.bit_count() <= 1

# n = len(string)
# Time Complexity: O(n)
# Space Complexity: O(1)


class TestPalindromePermutation:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_valid_palindrome(self):
        assert self.s.palindrome_permutation("No lemon no melon") is True
        assert self.s.palindrome_permutation(
            "Dormitory dirty room yoo") is True

    def test_invalid_palindrome(self):
        assert self.s.palindrome_permutation(
            "Never odd or even close") is False
        assert self.s.palindrome_permutation("test case fail") is False
