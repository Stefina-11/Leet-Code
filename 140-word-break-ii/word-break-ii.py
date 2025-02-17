class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)  # Convert wordDict to a set for O(1) lookups
        memo = {}  # Memoization dictionary
        
        def backtrack(start):
            if start in memo:  
                return memo[start]
            if start == len(s):  
                return [""]  # Base case: return empty string when fully segmented
            
            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    rest_sentences = backtrack(end)
                    for sentence in rest_sentences:
                        sentences.append(word + (" " + sentence if sentence else ""))
            
            memo[start] = sentences  # Store result in memo
            return sentences
        
        return backtrack(0)

# Example usage:
solution = Solution()
print(solution.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))  
# Output: ["cats and dog", "cat sand dog"]

print(solution.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))  
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

print(solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  
# Output: []
