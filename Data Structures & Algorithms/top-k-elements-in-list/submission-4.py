class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for x in nums:
            if x not in d:
                d[x]=1
            d[x]+=1
        sorted_d=dict(sorted(d.items(),key=lambda p:p[1],reverse=True))
        L=list(sorted_d.keys())
        return L[:k]
        