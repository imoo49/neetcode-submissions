class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        d1={}
        for x in nums:
            if x not in d1:
                d1[x]=1
            else:
                d1[x]+=1
        d2={}
        for i in range(1,n+1):
            d2[i]=[]
        for key in d1:
            d2[d1[key]].append(key)
        L=[]
        for f in range(n,0,-1):
            for nombre in d2[f]:
                L.append(nombre)
        return L[:k]