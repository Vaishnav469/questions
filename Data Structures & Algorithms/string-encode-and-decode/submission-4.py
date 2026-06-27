class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i, n in enumerate(strs):
            length = len(n)
            result = result + str(length) + "#" + n
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "#":
                length = length + s[i]
                i += 1
            i += 1
            length = int(length)
            word = ""
            for j in range(i, i + length):
                word = word + s[j]
            result.append(word)
            i += length

        return result



