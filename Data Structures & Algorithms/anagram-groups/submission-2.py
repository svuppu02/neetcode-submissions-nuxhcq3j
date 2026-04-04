from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for s in strs:
            sorted_word = ''.join(sorted(s))
            grouped[sorted_word].append(s)
        return list(grouped.values())
            

            

        