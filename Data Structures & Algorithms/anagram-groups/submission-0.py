class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len (strs)
        visited=[False]*n
        L=[]
        if n<1 or n>1000:
            return NUll
        for i in range(0,n):
            if len(strs[i])<0 or len (strs[i])>100:
                return False
            if not visited[i]:
                R=[strs[i]]
                visited[i] = True 
                j=i+1
                while j<n:
                    if sorted(strs[i])==sorted(strs[j]):
                        R.append(strs[j])
                        visited[j] = True
                    j=j+1
                L.append(R)    
        return L