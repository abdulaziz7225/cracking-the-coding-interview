class Solution:
    def one_away(self, s1: str, s2: str) -> bool:
        if abs(len(s1) - len(s2)) > 1:
            return False

        if len(s1) < len(s2):
            shorter, longer = s1, s2
        else:
            shorter, longer = s2, s1

        ptr1, ptr2 = 0, 0
        mismatch_found = False
        while ptr1 < len(shorter) and ptr2 < len(longer):
            if shorter[ptr1] == longer[ptr2]:
                ptr1 += 1
            elif mismatch_found:
                return False
            else:
                mismatch_found = True
                if len(shorter) == len(longer):
                    ptr1 += 1
            ptr2 += 1
        return True

# n = max(len(s1), len(s2))
# Time Complexity: O(n)
# Space Complexity: O(1)


class TestOneAway:
    @classmethod
    def setup_class(cls):
        cls.s = Solution()

    def test_replace_character(self):
        assert self.s.one_away("pale", "bale") == True
        assert self.s.one_away("pale", "bake") == False
        assert self.s.one_away("edit", "view") == False
        assert self.s.one_away("integral", "triangle") == False
        assert self.s.one_away("abc", "axc") == True

    def test_insert_character(self):
        assert self.s.one_away("abc", "abxc") == True
        assert self.s.one_away("abc", "abcyx") == False
        assert self.s.one_away("", "a") == True
        assert self.s.one_away("", "ab") == False
        assert self.s.one_away("abc", "abcd") == True
        assert self.s.one_away("abc", "abcdx") == False

    def test_remove_character(self):
        assert self.s.one_away("pale", "ple") == True
        assert self.s.one_away("pales", "pale") == True
        assert self.s.one_away("a", "") == True
        assert self.s.one_away("abc", "ab") == True
        assert self.s.one_away("abcd", "ac") == False
