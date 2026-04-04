class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        for i in range(len(nums)):
            ignore = i
            prod = 1
            for j in range(len(nums)):
                if j == ignore:
                    continue
                prod *= nums[j]
            
            res[i] = prod
        
        return res



        