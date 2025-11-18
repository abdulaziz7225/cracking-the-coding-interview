# Solution 1
class Solution:
    def check_permutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        s1_chars = dict()
        s2_chars = dict()
        for i in range(len(s1)):
            s1_chars[s1[i]] = s1_chars.get(s1[i], 0) + 1
            s2_chars[s2[i]] = s2_chars.get(s2[i], 0) + 1

        for key, val in s1_chars.items():
            if key not in s2_chars or s2_chars[key] != val:
                return False
        return True

# n = len(s1) = len(s2), c = number of unique characters (c = 128 for ASCII character)
# Time Complexity: O(n + c) ==> O(n)
# Space Complexity: O(2 * c) ==> O(c)


class TestCheckPermutation:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_different_length_strings(self):
        assert self.s.check_permutation("terminal", "selection") is False

    def test_anagram_words(self):
        assert self.s.check_permutation("integral", "triangle") is True

    def test_non_anagram_words(self):
        assert self.s.check_permutation("understand", "management") is False
