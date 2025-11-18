class Solution:
    def string_rotation(self, s1: str, s2: str) -> bool:
        if len(s1) == len(s2) != 0:
            return self.is_substring(s2 * 2, s1)
        return False

    def is_substring(self, string, substring) -> bool:
        return string.find(substring) != -1

# n = length(s1)
# Time Complexity: O(2 * n + 2 * n) ==> O(n)
# Space Complexity: O(2 * n) ==> O(n)


class TestStringRotation:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_string_rotation(self):
        assert self.s.string_rotation("waterbottle", "erbottlewat") is True
        assert self.s.string_rotation("apple", "pleap") is True
        assert self.s.string_rotation("camera", "macera") is False
