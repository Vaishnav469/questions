class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashmap = {}
        for prereq in prerequisites:
            if prereq[0] not in hashmap:
                hashmap[prereq[0]] = []
            hashmap[prereq[0]].append(prereq[1])
        
        def dfs(num, visit):
            if num not in hashmap:
                return True
            result = True
            for n in hashmap[num]:
                if n in visit:
                    return False
                visit.add(n)
                result = result and dfs(n, visit)
                visit.remove(n)
            return result
                
                

            
        boolean = True
        for i in range(numCourses):
            visit = set()
            visit.add(i)
            boolean = boolean and dfs(i, visit)
        return boolean
        

            