expenses = {
    "Food": [120,90,80],
    "Utilities": [1102,109,330],
    "Clothes": [5000,2000,300]
}

# function to calculate the total money spent
def Total_expense(expenses):
    total_expense = 0
    for i in expenses:
        total_expense += sum(expenses[i])
    return total_expense

# function to calculate category wise expenses
def category_wise_expense(expenses):
    for i in expenses:
        print("You Spent",sum(expenses[i]),"on",i)
    
# function to calculate highest spending category
def highest_spending_category(expenses):
    highest_expense = float('-inf')
    highest_category = ""
    for i in expenses:
        if sum(expenses[i])>highest_expense:
            highest_expense=sum(expenses[i])
            highest_category=i
    return highest_category


print(Total_expense(expenses))
category_wise_expense(expenses)
print(highest_spending_category(expenses))

