class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ##each course and each prerequisite is connected with directed edge
        #DFS lets us solve recursively: To finish Course A, can I finish all of Course A's prerequisites? To finish Course B (A's prereq), can I finish all of B's prerequisites?
        #if there's a cycle - infinite loop, return False
        #if we hit a dead end, done recursion - return True
        
        #builds an adjacency list to map course with prereq
        preMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        #hashset to track visited to detect cycles
        visiting = set()

        #dfs helper method
        def dfs(course):
            #base cases
            if course in visiting: #cycle detected
                return False
            if preMap[course] == []: #if no prereq
                return True
            visiting.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course) #remove the current path so we start new
            preMap[course] = [] #After successfully processing a course, clear its prerequisite list (mark as done).
            return True

        #iterate thr all components
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True