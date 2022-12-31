import pandas as pd
import student_module as s
import re
import Examination_module as exam


def create_batch(batch_id, batch_name, department, list_courses, list_students):
    df = pd.read_csv("batch.csv")
    df.set_index(["Batch ID"], inplace=True)
    df.loc[f"{batch_id}"] = [batch_name,department,list_courses,list_students]
    df.to_csv("batch.csv")
    print(df)

def get_lst_of_students(batch_id):
    #this function will give the list of students of the batch given with name roll etc

    df = pd.read_csv("batch.csv")
    df.set_index(["Batch ID"], inplace=True)
    lst_students = df.loc[f"{batch_id}"]["List Of Students"]
    starting_id = int((re.findall(".....([0-9][0-9]):", lst_students))[0])
    ending_id = int((re.findall(":.....([0-9][0-9])", lst_students))[0])
    df2 = pd.DataFrame({"Student ID":[],"Name":[],"Roll":[]})
    df2.set_index(["Student ID"], inplace=True)
    for i in range(starting_id, ending_id + 1):
        if i < 10:
            i = "0" + str(i)
        details = s.get_student(f"{batch_id}{i}")
        df2.loc[f"{batch_id}{i}"] = [details["Name"], details["Roll"]]
    print(df2)
    return df2

def view_performance(batch_id,print2=False):
    df = pd.read_csv("batch.csv")
    df.set_index(["Batch ID"], inplace=True)
    lst_students = df.loc[f"{batch_id}"]["List Of Students"]
    starting_id = int((re.findall(".....([0-9][0-9]):", lst_students))[0])
    ending_id = int((re.findall(":.....([0-9][0-9])", lst_students))[0])
    df2 = pd.DataFrame({"Student ID": [], "Name": [], "Roll": [], "Marks":[]})
    df2.set_index(["Student ID"], inplace=True)
    percent_lst = []
    for i in range(starting_id, ending_id + 1):
        if i < 10:
            i = "0" + str(i)
        details = s.get_student(f"{batch_id}{i}")
        percent = exam.get_report(f"{batch_id}{i}")
        df2.loc[f"{batch_id}{i}"] = [details["Name"], details["Roll"], f"{percent}%"]
        percent_lst.append(percent)
    if print2 == True:
        print(df2)
    return percent_lst

