import pandas as pd
import student_module as s

def add_course(course_id, dict_marks):
    exam = pd.read_csv("examination.csv")
    lst_main = list(exam["Student ID"])
    lst = []
    for id in lst_main:
        for key, value in dict_marks.items():
            if key == id:
                lst.append(value)
                break
    exam[course_id] = lst
    exam.to_csv("examination.csv", index=False)

def add_student(student_id, lst):
    exam = pd.read_csv("examination.csv")
    f = open("examination.csv", "a")
    f.write(f"{student_id},")
    for i in range(len(lst) - 1):
        f.write(f"{lst[i]},")
    f.write(f"{lst[len(lst) - 1]}\n")
    f.close()

def get_grades(j):
    j = int(j)
    if j>=90:
        grade = "A"
    elif j>=80:
        grade = "B"
    elif j>=70:
        grade = "C"
    elif j>=60:
        grade = "D"
    elif j>=50:
        grade = "E"
    else:
        grade = "F"
    return grade

def get_report(student_id, print=False):
    exam = pd.read_csv("examination.csv")
    exam.set_index(["Student ID"], inplace=True)
    marks = dict(exam.loc[student_id])
    # print(marks)
    name = s.get_student(student_id)["Name"]
    if print == True:
        f = open(f"{name}'s report", "w")
        f.write(f"Subject   Marks    Grades\n")
    total = 0
    for i,j in marks.items():
        grade = get_grades(j)
        total += int(j)
        if print == True:
            f.write(f"{i}       {j}         {grade}\n")
    percent = (total / (len(marks) * 100)) * 100
    if percent >= 50:
        if print == True:
            f.write("PASS\n")
    else:
        if print == True:
            f.write("FAIL\n")
    if print == True:
        f.close()
    return percent



