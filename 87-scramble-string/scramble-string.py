from functools import wraps

# Custom memoization decorator since lru_cache is not available in Python 2
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

class Solution:
    def isScramble(self, s1, s2):  # Removed type hints for Python 2 compatibility
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):  # Quick check to eliminate invalid cases
            return False
        
        @memoize  # Using our custom memoization function
        def dfs(s1, s2):
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):  # If different chars, return False
                return False
            
            n = len(s1)
            for i in range(1, n):  # Try splitting at different positions
                # Case 1: No Swap
                if dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:]):
                    return True
                # Case 2: Swap
                if dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i]):
                    return True
            
            return False
        
        return dfs(s1, s2)

# Test cases
solution = Solution()
print solution.isScramble("great", "rgeat")  # Output: True
print solution.isScramble("abcde", "caebd")  # Output: False
print solution.isScramble("a", "a")  # Output: True
