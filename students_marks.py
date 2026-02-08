students = {
    "Anita":78,
    "Sunita": 93,
    "Priya": 42,
    "Aaryan": 66,
    "Namit": 100
}

# function to caulculate average of studenst
def calculate_average(marks_dict):
    sum_of_marks = 0
    for i in marks_dict:
        sum_of_marks+=marks_dict[i]
    return sum_of_marks/len(marks_dict)

# function to get the topper of the class
def find_topper(marks_dict):
    max_marks = float('-inf')
    topper = ""
    for i in marks_dict:
        if marks_dict[i]>max_marks:
            max_marks=marks_dict[i]
            topper=i
    return topper

# function to find students who have scored more then the average of the class
def find_above_average(marks_dict):
    average = calculate_average(marks_dict)
    above_average_students = []
    for i in marks_dict:
        if marks_dict[i]>average:
            above_average_students.append(i)
    return above_average_students



print(calculate_average(students))
print(find_topper(students))
print(find_above_average(students))
