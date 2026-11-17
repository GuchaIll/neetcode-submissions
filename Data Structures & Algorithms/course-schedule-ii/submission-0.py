class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #Step 1: Building the adjencency list first
        dependencies = defaultdict(list)
        for course, dep in prerequisites:
            dependencies[course].append(dep)

        #dfs to traverse and store all possible combinations
        #no double traversal
        comb = []
        #course fully processed and added to comb
        visited = set()
        cycle = set() #courses in teh current recursion track

        def dfs( course):
    #course in current path readded, detected a cycle
            if course in cycle:
                #false means need to take course as prereq of a course not taken, but cycle is created because the course is previously required 
                return False    

            #why is it only for course in visited do we directly return true, #this course is already processed, "taken"
            if course in visited:
                return True

            cycle.add(course)

            #visit all prereq first
            for dep in dependencies[course]:
                if not dfs(dep):
                    return False
            
            cycle.remove(course)
            visited.add(course)

            comb.append(course)
            return True

        #iterate through any feasible starting points
        for i in range(numCourses):
            if not dfs( i):
                return []

        return comb
