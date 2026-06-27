class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) +  "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        array = []
        
        i = 0

        while i < len(s):
            num = ""
            k = i
            while k < len(s):
                if s[k] == '#':
                    break
                num += s[k]
                k+=1
            numlen = len(num)
            
            num = int(num)
            string = ""
            for j in range(num):
                string += s[j + i + 1 + numlen]
            array.append(string)
            i = i + num + 1 + numlen


        return array

