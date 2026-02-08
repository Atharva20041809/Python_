file = open('./expenses.txt','r')
lines = file.readlines()
expenses = {}
for text in lines:
    category, expense = text.split(',')
    expenses[category]=int(expense)

print(expenses)

file.close()
