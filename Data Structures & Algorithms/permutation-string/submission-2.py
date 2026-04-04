class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_sorted = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                sub = s2[i:j+1]
                sub = sorted(sub)
                if sub == s1_sorted:
                    return True
        return False
            
        