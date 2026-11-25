class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for mot in strs:
            key="".join(sorted(mot))
            if key not in d:
                d[key]=[]
            d[key].append(mot)
        L=list(d.values())
        return L

            
        