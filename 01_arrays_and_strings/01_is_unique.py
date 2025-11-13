# Solution 1: With hash set
class Solution1:
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


# Solution 2: Without additional data structure
# This solution assumes that string has only lowercase English letters (a-z)
class Solution2:
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


class TestIsUniqueSolution1:
    @classmethod
    def setup_class(cls):
        cls.s = Solution1()

    def test_unique(self):
        assert self.s.is_unique("background") == True

    def test_not_unique(self):
        assert self.s.is_unique("successful") == False


class TestIsUniqueSolution2:
    @classmethod
    def setup_class(cls):
        cls.s = Solution2()

    def test_unique(self):
        assert self.s.is_unique("exclusion") == True

    def test_not_unique(self):
        assert self.s.is_unique("appearance") == False
