class Solution:
    def string_compression(self, s: str) -> str:
        curr_char = s[0]
        count = 0
        compressed_parts = []

        for char in s:
            if char != curr_char:
                compressed_parts.append(curr_char + str(count))
                curr_char = char
                count = 0
            count += 1

        compressed_parts.append(curr_char + str(count))
        compressed_string = "".join(compressed_parts)

        return min(s, compressed_string, key=len)

# n = len(s)
# join() function takes O(n) time in the worst case
# Time Complexity: O(2 * n) ==> O(n)
# Space Complexity: O(2 *n) ==> O(n)


class TestStringCompression:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_returns_shorter_version(self):
        assert self.s.string_compression("aabcccccaaa") == "a2b1c5a3"
        assert self.s.string_compression("aaabb") == "a3b2"
        assert self.s.string_compression("cccccc") == "c6"

    def test_returns_original(self):
        assert self.s.string_compression("abc") == "abc"
        assert self.s.string_compression("aabb") == "aabb"
        assert self.s.string_compression("abababab") == "abababab"
        assert self.s.string_compression("a") == "a"
