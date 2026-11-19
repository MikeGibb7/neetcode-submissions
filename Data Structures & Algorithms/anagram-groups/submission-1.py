class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di = defaultdict(list)
        for st in strs:
            sort_st = "".join(sorted(st))
            di[sort_st].append(st)
        
        return list(di.values())