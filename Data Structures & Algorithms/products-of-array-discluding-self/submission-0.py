class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = []
        for i in range(n):
            current_position = 1
            for j in range(n):
                if i!=j:
                    current_position*=nums[j]
            res.append(current_position)
        return res