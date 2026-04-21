class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(num_courses)}
        for course, prereq in prerequisites:
            pre_map[course].append(prereq)

        visiting = set()
        def dfs(course):
            if course in visiting:
                # cycle detected
                return False
            if pre_map[course] == []:
                return True

            visiting.add(course)
            for prereq in pre_map[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)

            return True

        for course in range(num_courses):
            if not dfs(course):
                return False

        return True