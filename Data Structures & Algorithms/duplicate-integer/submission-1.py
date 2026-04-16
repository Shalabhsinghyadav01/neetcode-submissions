class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for num in nums: 
            if num in hash_table:
                hash_table[num]+=1
            else: 
                hash_table[num] = 1 
        for count in hash_table.values():
            if count > 1:
                return True 
        return False
           