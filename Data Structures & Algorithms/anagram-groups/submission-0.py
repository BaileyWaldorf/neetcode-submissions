class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26
            
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            
            if groups.get(key):
                groups[key].append(word)
            else:
                groups[key] = [word]
        
        return list(groups.values())