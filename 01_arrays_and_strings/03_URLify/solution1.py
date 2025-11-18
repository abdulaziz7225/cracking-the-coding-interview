class Solution:
    def urlify(self, string: str, true_length: int) -> str:
        chars = list(string)

        space_count = 0
        for read_idx in range(true_length):
            if string[read_idx] == " ":
                space_count += 1

        read_idx = true_length - 1
        write_idx = true_length + 2 * space_count - 1

        for read_idx in range(true_length - 1, -1, -1):
            if chars[read_idx] == " ":
                chars[write_idx - 2] = "%"
                chars[write_idx - 1] = "2"
                chars[write_idx] = "0"
                write_idx -= 3
            else:
                chars[write_idx] = chars[read_idx]
                write_idx -= 1

        return "".join(chars)

# n = true_length, m = total_length
# In the worst case of all spaces, n <= m <= 3 * n
# Time Complexity: O(2 *(n + m)) ==> O(n)
# Space Complexity: O(m)


class TestURLify:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_standard_case(self):
        # Input length: 13, Buffer needed: 13 + (2 spaces * 2 extra chars) = 17
        input_str = "Mr John Smith    "
        assert self.s.urlify(input_str, 13) == "Mr%20John%20Smith"

    def test_single_space(self):
        # Input length: 5, Buffer needed: 5 + 2 = 7
        input_str = "Hi Vd  "
        assert self.s.urlify(input_str, 5) == "Hi%20Vd"

    def test_leading_space(self):
        # Input length: 4 (" a b"), Buffer needed: 4 + (2*2) = 8
        input_str = " a b    "
        assert self.s.urlify(input_str, 4) == "%20a%20b"

    def test_trailing_space(self):
        # Space at the very end of the "true" string
        # Input length: 4 ("a b "), Buffer needed: 4 + (2*2) = 8
        input_str = "a b     "
        assert self.s.urlify(input_str, 4) == "a%20b%20"

    def test_consecutive_spaces(self):
        # Input length: 5 ("a  b"), Buffer needed: 5 + (2 spaces * 2) = 9
        input_str = "a  b    "
        assert self.s.urlify(input_str, 4) == "a%20%20b"

    def test_no_spaces(self):
        input_str = "nospaces"
        assert self.s.urlify(input_str, 8) == "nospaces"

    def test_empty_string(self):
        input_str = ""
        assert self.s.urlify(input_str, 0) == ""

    def test_only_spaces(self):
        # String is just two spaces
        # Input length: 2, Buffer needed: 2 + 4 = 6
        input_str = "      "
        assert self.s.urlify(input_str, 2) == "%20%20"
