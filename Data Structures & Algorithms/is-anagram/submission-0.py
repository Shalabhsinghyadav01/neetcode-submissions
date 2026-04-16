class Solution:
    def hm(self,st):
        self.st = st
        hash_table = {}
        for i in st: 
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] =1
        return hash_table 
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash_table = self.hm(s)
        t_hash_table = self.hm(t)
        if s_hash_table == t_hash_table:
            return True 
        return False 
