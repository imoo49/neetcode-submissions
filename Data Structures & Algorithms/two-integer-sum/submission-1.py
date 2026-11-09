class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=[]
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i]+nums[j]==target and i!=j:
                    L.append(i)
                    L.append(j)
                    return L            
        