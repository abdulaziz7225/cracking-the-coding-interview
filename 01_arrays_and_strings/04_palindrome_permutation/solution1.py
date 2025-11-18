# Solution 1: Using hashmap
class Solution:
    def palindrome_permutation(self, string: str) -> bool:
        freq_count = dict()
        for char in string:
            if char.isalpha():
                char = char.lower()
                freq_count[char] = freq_count.get(char, 0) + 1

        odd_freq = 0
        for freq in freq_count.values():
            if freq % 2 == 1:
                if odd_freq:
                    return False
                odd_freq += 1
        return True

# n = len(string), c = 52 for a-z and A-Z letters
# Time Complexity: O(n + c) ==> O(n)
# Space Complexity: O(c) ==> O(1)


class TestPalindromePermutation:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_valid_palindrome(self):
        assert self.s.palindrome_permutation("Tact Coa") == True
        assert self.s.palindrome_permutation("Red rum sir is murder") == True

    def test_invalid_palindrome(self):
        assert self.s.palindrome_permutation(
            "This is not a palindrome") == False
        assert self.s.palindrome_permutation(
            "Random words make nothing") == False
