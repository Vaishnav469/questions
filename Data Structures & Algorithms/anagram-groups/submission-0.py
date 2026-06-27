class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for i in range(len(strs)):
            array = [0] * 26
            for j in range(len(strs[i])):
                array[ord(strs[i][j]) - ord('a')] += 1
            
            if tuple(array) in hashmap.keys():
                hashmap[tuple(array)].append(strs[i])
            else:
                hashmap[tuple(array)] = [strs[i]]

        return hashmap.values()