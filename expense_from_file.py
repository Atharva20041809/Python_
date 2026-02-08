file = open('./expenses.txt','r')
lines = file.readlines()
expenses = {}
for text in lines:
    category, expense = text.strip().split(',')
    expenses[category]=int(expense)

print(f"This is the expenses: ${expenses} extracted from another file.")

file.close()
