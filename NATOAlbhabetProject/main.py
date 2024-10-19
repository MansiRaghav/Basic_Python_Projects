student_dict ={
    "student" : ["Anjela","mansi","preeti","shreya"],
    "scores"  : [ 24 ,60 ,78 ,59]
}


import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index,row) in student_data_frame.iterrows():
    print(row)
    if row.student == "Anjela":
        print(row.scores)
