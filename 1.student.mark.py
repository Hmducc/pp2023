#Data Called
student=[]
course=[]
mark=[]


#input course's information
y= int(input("Number of course: "))
print("Course number: ", y)
for i in range(y):
    course.append((
        int(input("Course ID: ")),
        str(input("Course name: "))
    ))

#input student's information
x=int(input("Number of student in class is: "))
print("Number of student:", x)
for i in range(x):
    student.append((
     str(input("Student name: ")),
     str(input("Student ID: ")),
     str(input("Student DoB: "))
    ))
#input student's mark
    student_mark=[]
    student_name=[]
for subject in course: 
    student_mark.append(input(f"Course {course[subject]} mark: "))
    for someone in student:
        student_name.append(input(f"Student {student[someone]}'s course {subject[1]} mark:  "))
    student.append(student_name)
mark.append(student_mark)

