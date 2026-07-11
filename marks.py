class Student:
    def __init__(self):
        self.grades=[]
    
    def add(self,grade):
        self.grades.append(grade)

    def remove(self,grade):
        self.grades.remove(grade)

    def __str__(self):
        return(str(self.highest))

    @property
    def average(self):
        i=0
        j=0
        for grade in self.grades:
            i+=grade
            j+=1
        return(i/j)
    
    @property
    def highest(self):
        i=self.grades[0]
        for grade in self.grades:
            if(grade>i):
                i=grade
        return i
    
stu=Student()
stu.add(99)
stu.add(99)
stu.add(100)
stu.add(100)
stu.remove(100)
stu.add(95)
stu.add(99)
print(stu)