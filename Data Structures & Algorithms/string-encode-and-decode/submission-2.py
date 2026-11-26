class Solution:

    def encode(self, strs: List[str]) -> str:
        L = ""
        for word in strs:
            L+=str(len(word))+"#"+word
        return L
    def decode(self, s: str) -> List[str]:
        R=[]
        i=0
        while i<len(s):
            j=s.find("#",i)
            length=int(s[i:j])
            R.append(s[j+1:j+length+1])
            i=j+length+1
        return R


