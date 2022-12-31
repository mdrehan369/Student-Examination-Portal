import re
import student_module as s
import Examination_module as exam
import course_module as c
import department_module as depart
import batch_module as batch

greet = "Welcome To Main Menu\n"
options_main = "Please select the section that you want to go in\n" \
          "Press 1 to go to Student Section\n" \
          "Press 2 to go to Course Section\n" \
          "Press 3 to go to Department Section\n" \
          "Press 4 to go to Batch Section\n" \
               "Press 0 to exit from program\n"

options_student = "Please select the action you want to perform\n" \
                  "Press 1 to add a student\n" \
                  "Press 2 to update details of a student\n" \
                  "Press 3 to delete a student from the database\n" \
                  "Press 4 to get the report of a student\n" \

options_course = "Please select the action you want to perform\n" \
                 "Press 1 to add a course\n" \
                 "Press 2 to view performance of students in that course\n" \

options_batch = "Please select the action you want to perform\n" \
                "Press 1 to add a batch\n" \
                "Press 2 to get list of students who studies in the given batch\n" \
                "Press 3 to view performance of all students in the given batch\n" \

options_depart = "Please select the action you want to perform\n" \
                 "Press 1 to add a department\n" \
                 "Press 2 to view batches in the given department\n" \
                 "Press 3 to view average performance of all batches in the given department\n" \
                 "Press 4 to plot a graph of performances of all batches in percentage versus batches\n" \

def check_stu_id(student_id):
    patt = re.findall("[A-Z]+[0-9]{4}", student_id)
    if len(patt) == 1:
        return True
    else:
        return False

def check_roll(roll):
    patt = re.findall("[0-9]+", roll)
    if len(patt) == 1:
        return True
    else:
        return False

def check_batch(batch):
    patt = re.findall("[A-Z]+[0-9]{2}", batch)
    if len(patt) == 1:
        return True
    else:
        return False

def check_name(student_id):
    try:
        stu = s.get_student(student_id)
    except:
        return False
    if stu != None:
        return True
    else:
        return False

while 1:
    #Main menu
    print(greet)
    first_inp = int(input(options_main))
    if first_inp == 1:
        print("Welcome to Student Section\n")
        second_inp = int(input(options_student))
        if second_inp == 1:
            details = input("Enter the Student ID, Name, Roll and Batch all separated by commas and no space in between commas\n")
            try:
                details = details.split(",")
                if check_stu_id(details[0]) and check_roll(details[2]) and check_batch(details[3]):
                    s.create_student(details[0],details[1],details[2],details[3])
                else:
                    print("Check your details. It does not match the type of data.\n")
            except:
                print("Something went wrong. Please try again later.\n")
            continue
        elif second_inp == 2:
            details = input("Enter the updated details of the student i.e, student id, name, roll and batch separated by only commas\n")
            details = details.split(",")
            if check_stu_id(details[0]) and check_roll(details[2]) and check_batch(details[3]) and check_name(details[0]):
                s.update_details(details[0], details[1], details[2], details[3])
            else:
                print("Check your details. It does not match the type of data.\n")
        elif second_inp == 3:
            detail = input("Enter the student id that you want to delete\n")
            if check_stu_id(detail):
                s.delete_student(detail)
            else:
                print("Check your details. It does not match the type of data.\n")
        elif second_inp == 4:
            detail = input("Enter the student id that you want to get report of\n")
            if check_stu_id(detail):
                try:
                    exam.get_report(detail, True)
                    print("Please check your directory, the report had been saved there with the student's name\n")
                except:
                    print("Please check the student id you entered")
            else:
                print("Check your details. It does not match the type of data.\n")
        else:
            print("Invalid input\n")
            continue
    elif first_inp == 2:
        print("Welcome to course section\n")
        second_inp = int(input(options_course))
        if second_inp == 1:
            ID = input("Enter the course ID\n")
            name = input("Enter the course name\n")
            number = int(input("Enter the number of students you want to register for the course\n"))
            dic = {}
            i = 0
            while i != number:
                id = input(f"Enter the Student ID of student number {i+1} : ")
                try:
                    mark = int(input("Enter the marks : "))
                except:
                    print("Marks should be an integer or float value\n")
                    continue
                if check_stu_id(id) and check_name(id):
                    dic[id] = mark
                    i += 1
                else:
                    print("Could not register the last student. Either the student id is invalid or the student is not register in the database. Please input valid details\n")
                    continue
            c.add_course(ID, name, dic)
        elif second_inp == 2:
            id = input("Enter the course id\n")
            try:
                c.view_performance(id)
            except:
                print("Invalid course id or the course is not yet registered\n")
        else:
            print("Invalid input\n")


    elif first_inp == 3:
        print("Welcome to department section\n")
        second_inp = int(input(options_depart))
        if second_inp == 1:
            id = input("Enetr the department ID : ")
            name = input("Enter the department name : ")
            batches = input("Enter the list of batches separated by a colon (:) only withot extra spacing : ")
            depart.create_department(id, name, batches)

        elif second_inp == 2:
            id = input("Enter the department id : ")
            try:
                depart.view_batches(id, True)
            except:
                print("The id is invalid or the department has not been registered\n")
        elif second_inp == 3:
            id = input("Enter the department id : ")
            try:
                depart.view_avg_performance_of_batches(id)
            except:
                print("The id is invalid or the department has not been registered\n")
        elif second_inp == 4:
            id = input("Enter the department id : ")
            try:
                depart.plot_performance(id)
            except:
                print("The id is invalid or the department has not been registered\n")
        else:
            print("Invalid input\n")

    elif first_inp == 4:
        print("Welcome to batch section\n")
        second_inp = int(input(options_batch))
        if second_inp == 1:
            id = input("Enter the batch id : ")
            name = input("Enter the batch name : ")
            dep = input("Enter the department ID")
            lst_courses = input("Enter the list of courses separated by colons only (:) : ")
            lst_stu = input("Enter the list of students separated by colons only (:) : ")
            try:
                batch.create_batch(id, name, dep, lst_courses, lst_stu)
            except:
                print("Details are invalid")
        elif second_inp == 2:
            id = input("Enter the batch id : ")
            try:
                batch.get_lst_of_students(id)
            except:
                print("Invalid details")
        elif second_inp == 3:
            id = input("Enter the batch id : ")
            try:
                batch.view_performance(id, True)
            except:
                print("Invalid details")
        else:
            print("invalid input")
    elif first_inp == 0:
        break

    else:
        print("Invalid input")