# Solution 1: With hash set
class Solution:
    def is_unique(self, string: str) -> bool:
        unique_set = set()
        for char in string:
            if char in unique_set:
                return False
            unique_set.add(char)
        return True

# n = len(s), m = number of unique characters, it would be 128 for ASCII only characters
# Time Complexity: O(n)
# Space Complexity: O(m)


class TestIsUnique:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_unique(self):
        assert self.s.is_unique("background") is True

    def test_not_unique(self):
        assert self.s.is_unique("successful") is False
