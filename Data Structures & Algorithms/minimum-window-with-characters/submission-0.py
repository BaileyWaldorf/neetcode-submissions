class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)      # chars/counts we need from t
        window = {}            # chars/counts in current window

        have = 0               # number of chars whose required count is satisfied
        required = len(need)   # number of unique chars we need to satisfy

        left = 0
        best_len = float("inf")
        best_start = 0

        for right in range(len(s)):
            # Add current right character to the window
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # If this character is needed and we now have enough of it,
            # one requirement is satisfied
            if c in need and window[c] == need[c]:
                have += 1

            # While the window is valid, try shrinking it from the left
            while have == required:
                window_len = right - left + 1

                # Save best/smallest valid window
                if window_len < best_len:
                    best_len = window_len
                    best_start = left

                # Remove left character from the window
                left_char = s[left]
                window[left_char] -= 1

                # If removing it makes us fall below the needed count,
                # the window is no longer valid
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]