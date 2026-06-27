class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in range(len(strs)):
            count = [0] * 26
            word = strs[i]
            for j in word:
                count[ord(j) - ord('a')] += 1
            hashmap[tuple(count)].append(word)
        return list(hashmap.values())
