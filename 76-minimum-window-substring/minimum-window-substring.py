from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""
        
        # Frequency map for characters in t
        t_freq = Counter(t)
        required = len(t_freq)  # Number of unique characters in t to be matched

        # Pointers and variables for sliding window
        left, right = 0, 0
        formed = 0  # Number of characters that meet the required frequency
        window_counts = defaultdict(int)
        min_length = float("inf")
        min_window = (0, 0)  # Tuple to store the start and end of the smallest window

        while right < len(s):
            # Add the current character to the window
            char = s[right]
            window_counts[char] += 1

            # Check if the current character satisfies the condition for t
            if char in t_freq and window_counts[char] == t_freq[char]:
                formed += 1

            # Try to contract the window
            while left <= right and formed == required:
                char = s[left]

                # Update the minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = (left, right)

                # Remove the left character from the window
                window_counts[char] -= 1
                if char in t_freq and window_counts[char] < t_freq[char]:
                    formed -= 1

                left += 1  # Shrink the window

            # Expand the window
            right += 1

        # If no valid window is found, return an empty string
        return "" if min_length == float("inf") else s[min_window[0]:min_window[1] + 1]
