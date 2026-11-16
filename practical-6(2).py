
# Pandas Series and DataFrame
import pandas as pd

# Get number of students
n = int(input("Enter number of students: "))

rollno = []
names = []
departments = []
marks_list = []
index_list = []

# Get student details from user
for i in range(n):
    print("\nEnter Student", i + 1, "Details")

    r = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    mark = int(input("Enter Mark: "))

    rollno.append(r)
    names.append(name)
    departments.append(dept)
    marks_list.append(mark)
    index_list.append(chr(65 + i))

# Create a Pandas Series
marks = pd.Series(
    marks_list,
    index=index_list
)

print("\n--- Pandas Series ---")
print(marks)

# Create a Pandas DataFrame from a dictionary
data = {
    "RollNo": rollno,
    "Name": names,
    "Department": departments,
    "Mark": marks_list
}

df = pd.DataFrame(data)

print("\n--- DataFrame ---")
print(df)

# DataFrame operations
print("\nAverage Mark:", round(df["Mark"].mean(), 2))

print("\nStudents scoring above 85:")
print(df[df["Mark"] > 85])
