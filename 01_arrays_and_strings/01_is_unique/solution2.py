# Solution 2: Without additional data structure
# This solution assumes that string has only lowercase English letters (a-z)
class Solution:
    def is_unique(self, string: str) -> bool:
        checker = 0
        for char in string:
            pos = ord(char) - ord("a")
            if checker & (1 << pos) != 0:
                return False
            checker |= 1 << pos
        return True

# Time Complexity: O(n * log(n))
# Space Complexity: O(c) ==> O(1)


class TestIsUnique:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_unique(self):
        assert self.s.is_unique("exclusion") is True

    def test_not_unique(self):
        assert self.s.is_unique("appearance") is False
