class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        di = {}
        for i in nums:
            di[i] = di.get(i,0) + 1
        sorted_di = sorted(di.items(), key=lambda item: item[1], reverse=True)
        li = list(sorted_di)
        li2 = []
        for i in range(k):
            x,y = li[i]
            li2.append(x)
        
        return li2