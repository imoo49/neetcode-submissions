class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=[]
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]+nums[i]==target and i!=j:
                    L.append(i)
                    L.append(j)
                    return L
        