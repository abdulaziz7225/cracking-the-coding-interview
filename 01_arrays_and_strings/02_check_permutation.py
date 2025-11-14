# Solution 1
class Solution1:
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


# Solution 2
class Solution2:
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


class TestCheckPermutationSolution1:
    @classmethod
    def setup_class(cls):
        cls.s = Solution1()

    def test_different_length_strings(self):
        assert self.s.check_permutation("terminal", "selection") == False

    def test_anagram_words(self):
        assert self.s.check_permutation("integral", "triangle") == True

    def test_non_anagram_words(self):
        assert self.s.check_permutation("understand", "management") == False


class TestCheckPermutationSolution2:
    @classmethod
    def setup_class(cls):
        cls.s = Solution2()

    def test_different_length_strings(self):
        assert self.s.check_permutation("management", "hospital") == False

    def test_anagram_words(self):
        assert self.s.check_permutation("mastering", "streaming") == True

    def test_non_anagram_words(self):
        assert self.s.check_permutation("announcement", "development") == False
