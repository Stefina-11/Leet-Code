class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        
        # Step 1: Place each number in its correct index if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]  # Swap
        
        # Step 2: Find the first missing positive number
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1  # If all numbers 1 to n are present, return n+1
