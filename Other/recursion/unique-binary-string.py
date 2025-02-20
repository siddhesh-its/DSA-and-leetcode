class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(nums)
        n = len(nums)
        
        def backtrack(num):
            if len(num) == n:
                if num not in seen:
                    return num
                return None # If it's already seen, backtrack
                    
             
            for char in "01": # Try adding '0' and '1'
                result = backtrack(num+char)
                if result != None: # If a valid result is found, propagate it up
                    return result
            
            return None # If no valid string is found, return None

        return backtrack("")

        # # O(N) O(1)
        # # Cantor's Diagonal Argument
        # # one bit different from all numbers - cannot be same
        # """
        # res = ""
        # for i in range(len(nums)):
        #     cur = nums[i][i]
        #     res += ("1" if cur == "0" else "0")
        
        # return res
# 1980. Find Unique Binary String
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 

# Example 1:

# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
# Example 2:

# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
# Example 3:

# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 

# Constraints:

# n == nums.length
# 1 <= n <= 16
# nums[i].length == n
# nums[i] is either '0' or '1'.
# All the strings of nums are unique.