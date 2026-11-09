class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        L=[]
        R=[]
        for x in nums:
            if x not in [elem[0] for elem in R]:
                 R.append((x, nums.count(x)))
        for j in range(len(R)):        
            for i in range(0,len(R)-1):
                if R[i+1][1] > R[i][1]:
                    R[i], R[i+1] = R[i+1], R[i]
        D=R[:k]
        for i in range(len(D)):
            L.append(D[i][0])
        return L
              