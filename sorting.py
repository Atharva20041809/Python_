expenses = {
    "Food":120,
    "Food":80,
    "Travel":50,
    "Entertainment":150,
    "Utilities":400
}

sorted_expenses = dict(sorted(expenses.items(),key= lambda item: item[1]))

print(sorted_expenses)