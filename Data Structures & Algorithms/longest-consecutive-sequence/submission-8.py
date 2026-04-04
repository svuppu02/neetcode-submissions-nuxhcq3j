class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for num in numSet:
            curr = num
            streak = 0
            while curr in numSet:
                curr += 1
                streak += 1
                
            res = max(res, streak)
        
        return res