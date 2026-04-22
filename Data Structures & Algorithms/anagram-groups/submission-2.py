class Solution:
    def hm(self,st):
        self.st = st
        hash_m = {}
        for i in st:
            if i in hash_m: 
                hash_m[i]+=1
            else:
                hash_m[i] = 1
        return hash_m
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            key =  tuple(sorted(self.hm(s).items()))
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        return list(hash_map.values())