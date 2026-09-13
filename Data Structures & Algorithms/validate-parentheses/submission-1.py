class Solution:
    def isValid(self, s: str) -> bool:
        chars = list(s)

        if len(chars) % 2 != 0:
            return False

        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        left = 0
        right = len(chars) - 1

        while left < right:
            if chars[left] not in pairs:
                return False

            if pairs[chars[left]] != chars[right]:
                return False

            left += 1
            right -= 1

        return True