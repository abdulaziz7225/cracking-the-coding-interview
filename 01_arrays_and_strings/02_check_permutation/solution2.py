# Solution 2
class Solution:
    def check_permutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        chars = [0] * 128
        for i in range(len(s1)):
            chars[ord(s1[i])] += 1
            chars[ord(s2[i])] -= 1

        for count in chars:
            if count != 0:
                return False
        return True

# n = len(s1) = len(s2), c = 128 for ASCII character
# Time Complexity: O(n + 2 * c) ==> O(n)
# Space Complexity: O(c)


class TestCheckPermutation:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_different_length_strings(self):
        assert self.s.check_permutation("management", "hospital") is False

    def test_anagram_words(self):
        assert self.s.check_permutation("mastering", "streaming") is True

    def test_non_anagram_words(self):
        assert self.s.check_permutation("announcement", "development") is False
