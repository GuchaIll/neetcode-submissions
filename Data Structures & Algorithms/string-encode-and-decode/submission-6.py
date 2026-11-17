class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += str(length) + "#" + word
        return encoded
        
    def decode(self, s: str) -> List[str]:
        curr = 0
        decoded = []
        while curr < len(s):
            length = 0
            while s[curr].isdigit():
                length = length*10 + int(s[curr])
                curr += 1
            curr += 1
            decoded.append(s[curr:curr+length])
            curr += length
        return decoded