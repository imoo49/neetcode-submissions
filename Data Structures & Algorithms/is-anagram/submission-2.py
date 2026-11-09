class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if n!=m:
            return False  
        for i in range (n):
            for j in range (m):
                if s[i]==t[j] and s.count(s[i])==t.count(t[j]):
                    break 
            else:
                return False    
        return True
                    