class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if not students:
            return 0
        elif not sandwiches:
            return len(students)

        rejections = 0
        num_studs = len(students)

        while rejections < num_studs:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                num_studs -= 1
                rejections = 0
            else:
                s = students.pop(0)
                students.append(s)
                rejections += 1

        return num_studs