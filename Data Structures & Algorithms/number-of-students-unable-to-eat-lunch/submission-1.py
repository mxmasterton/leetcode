class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        students_map = {0: 0, 1: 0}
        for student in students:
            students_map[student] += 1
            count += 1

        for sandwich in sandwiches:
            if students_map[sandwich] > 0:
                students_map[sandwich] -= 1
                count -= 1
            else:
                break

        return count