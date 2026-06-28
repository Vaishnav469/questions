class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {}
        for prereq in prerequisites:
            if prereq[0] not in hashmap:
                hashmap[prereq[0]] = []
            hashmap[prereq[0]].append(prereq[1])
        processed = set()
        def dfs(num, visit):
            if num not in hashmap or num in processed:
                return True
            result = True
            for n in hashmap[num]:
                if n in visit:
                    return False
                visit.add(n)
                if dfs(n, visit):
                    processed.add(n)
                else:
                    return False
                visit.remove(n)

            return True
            
        for i in range(numCourses):
            visit = set()
            visit.add(i)
            if not dfs(i, visit):
                return False
            processed.add(i)
        return True
        

            