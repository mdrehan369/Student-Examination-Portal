import pandas as pd
import student_module as s

def add_course(course_id, course_name, marks):
    marks = dict(marks)
    f = open("course.csv", "a")
    f.write(f"{course_id},{course_name},")
    for id,mark in marks.items():
        f.write(f"{id}:{mark}-")
    f.write("\n")
    f.close()

def view_performance(course_id):
    df = pd.read_csv("course.csv")
    df.set_index(["Course ID"], inplace=True)
    st = df.loc[course_id]["Marks Obtained"]
    data_lst = st.split("-")
    df2 = pd.DataFrame({"Student ID":[], "Name":[], "Roll":[], "Batch":[], "Marks":[]})
    df2.set_index(["Student ID"], inplace=True)
    for i in data_lst:
        if len(i) != 0:
            div = i.split(":")
            details = s.get_student(div[0])
            df2.loc[f"{div[0]}"] = [details["Name"], details["Roll"], details["Batch"], div[1]]
    print(df2)



