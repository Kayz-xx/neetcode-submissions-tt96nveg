class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += string
            encoded += "::="
        return encoded
        
    def decode(self, string) -> List[str]:
        decoded = string.split("::=")
        return decoded[:len(decoded)-1]