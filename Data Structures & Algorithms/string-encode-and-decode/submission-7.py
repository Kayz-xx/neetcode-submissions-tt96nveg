class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for string in strs:
            # Metadata: length + "#" + content
            encoded += str(len(string)) + "#" + string
        return encoded

    def decode(self, string: str) -> list[str]:
        if not string: return []
        
        i = 0
        res = []
        while i < len(string):
            j = i
            # Correctly handle variable length digits (1#, 10#, 100#)
            while string[j] != '#':
                j += 1
            
            size = int(string[i:j]) # Get the length
            
            # Start the word AFTER the '#' and take 'size' characters
            word = string[j + 1 : j + 1 + size]
            res.append(word)
            
            # Jump i to the start of the next length digit
            i = j + 1 + size 
            
        return res