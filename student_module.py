import pandas as pd
import re

class Student():

    def __init__(self, student_id, name, roll, batch):
        self.name = name
        self.roll = roll
        self.student_id = student_id
        self.batch = batch

    def update_csv(self):
        file = open("student.csv", "a")
        file.write(f"{self.student_id},{self.name},{self.roll},{self.batch}\n")
        file.close()

def get_student(student_id, print2 = False):
    df = pd.read_csv("student.csv")
    df.set_index(["Student ID"], inplace=True)
    details = dict(df.loc[student_id])
    if print2 == True:
        print(details)
    return details

def update_details(student_id, name, roll, batch):
    student_dp = pd.read_csv("student.csv")
    new = student_dp.set_index(["Student ID"])
    new.loc[student_id] = f"{name}", roll, batch
    new.to_csv("student.csv")


def create_student(student_id, name, roll, batch):
    s1 = Student(student_id, name, roll, batch)
    s1.update_csv()

def delete_student(student_id):
    student_df = pd.read_csv("student.csv")
    new = student_df.set_index(["Student ID"])
    new.drop(student_id, inplace=True)
    new.to_csv("student.csv")



