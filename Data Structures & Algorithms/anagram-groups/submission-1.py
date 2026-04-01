class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = defaultdict(list)
        for s in strs:
            sorted_string = ''.join(sorted(s))
            collection[sorted_string].append(s)
        
        return list(collection.values())