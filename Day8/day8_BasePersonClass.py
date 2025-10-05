
class InvalidMarksError(Exception):
    pass

class Person:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def __str__(self):
        return f"{self.name} (Roll {self.roll})"

class Student(Person):
    def __init__(self,name,roll,marks):
        super().__init__(name,roll)
        self.marks = self.validate_marks(marks)
    def validate_marks(self,marks):
        if len(marks) != 3:
            raise InvalidMarksError("Exactly 3 marks required")
        for m in marks:
            if not isinstance(m,(int,float))or m<0 or m>100:
                raise InvalidMarksError("Marks must be 0-100 nmeric values")
            return marks
    def total(self):
        return sum(self.marks)
    def average(self):
        return self.tolal()/ len(self.marks)
    def grade(self):
        avg=self.average()
        if avg >=90:return "A"
        if avg >=70:return "B"
        if avg >=50:return "C"
        return "F"
    def report_card(self):
        return(
            f"Nmae: {self.name}\n"
            f"Roll: {self.roll}\n"
            f"Marks: {self.marks}\n"
        )
class Athlete:
    def __init__(self,sport=None,level="School"):
        self.sport=sport
        self.level=level
    def athlete_info(self):
        if self.sport:
            return f"Sport: {self.sport} - Level: {self.level}"
        return ""
class StudentAthlete(Student,Athlete):
    def __init__(self,name,roll,marks,sport=None,level="School"):
        Student.__init__(self,name,roll,marks)
        Athlete.__init__(self,sport,level)
    def report_card(self):
        base = super().report_card()
        if self.sport:
            base += "\n" +self.athlete_info()
        return base
def input_marks():
    nums =input("enter 3 marks separated by space:").split()
    if len(nums) !=3:
        raise InvalidMarksError("Enter exactly 3 no:")
    marks = []
    for n in nums:
        marks.append(float(n))
    return marks
if __name__=="__main__":
    try:
        name=input("enter the name:")
        roll=int(input("enter the roll no:"))
        marks=input_marks()
        sport=input("enter sport(leave balnk if none):")
        student=StudentAthlete(name,roll,marks,sport if sport else None)
        print("\n--- Report card---")
        print(student.report_card())
    except InvalidMarksError as e:
        print("Error:",e)
    except ValueError:
        print("Error: Invalid number input")
    except InvalidMarksError as e:
        print("Error:",e)
    except ValueError:
        print("Error: Invalid number input")

