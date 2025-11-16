# Solution 1: Using hashmap
class Solution1:
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


# Solution 2: Using bit vector
class Solution2:
    def palindrome_permutation(self, string: str) -> bool:
        bit_vector = 0

        for char in string:
            if char.isalpha():
                char = char.lower()
                bit_vector ^= 1 << (ord(char) - ord("a"))

        return bit_vector.bit_count() <= 1

# n = len(string)
# Time Complexity: O(n)
# Space Complexity: O(1)


class TestPalindromePermutationSolution1:
    @classmethod
    def setup_class(cls):
        cls.s = Solution1()

    def test_valid_palindrome(self):
        assert self.s.palindrome_permutation("Tact Coa") == True
        assert self.s.palindrome_permutation("Red rum sir is murder") == True

    def test_invalid_palindrome(self):
        assert self.s.palindrome_permutation(
            "This is not a palindrome") == False
        assert self.s.palindrome_permutation(
            "Random words make nothing") == False


class TestPalindromePermutationSolution2:
    @classmethod
    def setup_class(cls):
        cls.s = Solution2()

    def test_valid_palindrome(self):
        assert self.s.palindrome_permutation("No lemon no melon") == True
        assert self.s.palindrome_permutation(
            "Dormitory dirty room yoo") == True

    def test_invalid_palindrome(self):
        assert self.s.palindrome_permutation(
            "Never odd or even close") == False
        assert self.s.palindrome_permutation("test case fail") == False
