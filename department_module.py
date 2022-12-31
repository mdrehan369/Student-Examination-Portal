import pandas as pd
import batch_module as b
import matplotlib.pyplot as plt

def create_department(depart_id, depart_name, lst_of_batches):
    df = pd.read_csv("department.csv")
    df.set_index(["Department ID"], inplace = True)
    df.loc[depart_id] = [depart_name, lst_of_batches]
    df.to_csv("department.csv")


def view_batches(depart_id, print2=False):
    df = pd.read_csv("department.csv")
    df.set_index(["Department ID"], inplace=True)
    batches = df.loc[depart_id][1]
    batches_lst = batches.split(":")
    for batch in batches_lst:
        if print2 == True:
            print(batch)
    return batches_lst

def get_avg_batch_marks(batch_id):
    marks = b.view_performance(batch_id)
    sum = 0
    for mark in marks:
        sum += mark
    avg = sum / len(marks)
    return round(avg, 2)

def view_avg_performance_of_batches(depart_id):
    batches = view_batches(depart_id)
    df = pd.DataFrame({"Batch ID":[], "Avg. Marks":[]})
    df.set_index(["Batch ID"], inplace=True)
    for batch in batches:
        marks = get_avg_batch_marks(batch)
        df.loc[batch] = [f"{marks}%"]
    print(df)

# view_avg_performance_of_batches("CSE")
def plot_performance(depart_id):
    batches = view_batches(depart_id)
    x = batches
    y = []
    for batch in batches:
        avg = get_avg_batch_marks(batch)
        y.append(avg)
    plt.plot(x, y)
    plt.xlabel = "Batch Name"
    plt.ylabel = "Average Percentage"
    plt.title = "Average Percentage Of All Students For Each Batch"
    plt.show()
