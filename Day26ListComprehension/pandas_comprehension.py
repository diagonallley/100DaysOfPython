import pandas

student_dict={
    "student":["Angela","James","Lily"],
    "score":[56,76,98]
}

student_df=pandas.DataFrame(student_dict)
# print(student_df)

# Iter rows

for (index, row) in student_df.iterrows():
    print(row.student) # Returns a series 