class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = {}
        for s in strs:
            sorted_string = ''.join(sorted(s))
            current = collection.get(sorted_string, [])
            current.append(s)
            collection[sorted_string] = current
        
        
        return list(collection.values())