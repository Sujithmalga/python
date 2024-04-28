class percentage:
    def __init__(self,marks:str,grade:str):
        self._marks = int(marks)
        self._grade = grade

    def marks(self):
        return self._marks
    def grade(self):
        return self._grade
    
class college:
    def __init__(self,student_id:str,
                 course:str,
                 extra_cultural:str):
        self._student_id = student_id
        self._course = course
        self._extra_cultural = extra_cultural

    


