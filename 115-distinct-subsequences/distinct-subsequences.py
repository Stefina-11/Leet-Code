class Solution:
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        prev = [0] * (n + 1)
        prev[0] = 1  # Base case: empty t can always be formed

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            curr[0] = 1  # Base case
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            prev = curr  # Move current row to previous
        
        return prev[n]

# Example usage:
solution = Solution()
print(solution.numDistinct("rabbbit", "rabbit"))  # Output: 3
print(solution.numDistinct("babgbag", "bag"))  # Output: 5
