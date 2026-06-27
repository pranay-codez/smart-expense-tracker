def add_expense():
    total_amnt = 0
    defined_category = input("Enter the  category from the following options (Food, Transport, Entertainment, Utilities, Other): ").lower()
    day = int(input("Enter the day of the expense (1-31): "))
    month = int(input("Enter the month of the expense (1-12): "))
    year = int(input("Enter the year of the expense (e.g., 2023): "))
    if defined_category not in ["food", "transport", "entertainment", "utilities", "other"]:
        print("Invalid category . Please chosee from the give options...")
        return
    expense={
        "category": defined_category,
        "amount": float(input("Enter the amount of the expense: ")),
        "date": [day , month , year]
    }
    total_amnt += expense["amount"]
    show_expenses = []
    show_expenses.append(expense)
    return show_expenses , total_amnt

def diplay_expenses(show_expenses):
    i=0
    while i<len(show_expenses):
        print (f"{show_expenses[i]}")
        i+=1


def total_expenses(amnt):
    return amnt

def categorize_expenses(data,cat_data):
    i=0
    while i<len(data):
        if data[i][0]["category"] == cat_data:
            print(f"{data[i]}")
        else:
            print("NO food expenses found.")
            
        i+=1
            

def monthly_summary(month,data):
    i=0
    if month>12 or month<1:
        print("Invalid month. Please enter a value between 1 and 12.")
        return
    print(f"Monthly Summary for Month: {month}")
    while i<len(data):
        if data[i][0]["date"][1] == month:
            print(f"{data[i]}")
        i+=1
    

           
            
           


def main():
    sum_amnt = 0
    result = []
    while True:
        switch = input("Enter your choice: \n1. Add Expense\n2. Display Expenses\n3. Total Expenses\n4. Categorize Expenses\n5. Monthly Summary\n6. Exit\n")
        if switch == '1':
            data , amnt_var = add_expense()
            result.append(data)
            sum_amnt += amnt_var

        elif switch == '2':
            diplay_expenses(result)
            
        elif switch == '3':
            total = total_expenses(sum_amnt)
            print(f"Total Expenses: {total}")

        elif switch == '4':
            cat_data = input("Enter the category to filter expenses (Food, Transport, Entertainment, Utilities, Other): ").lower()
            categorize_expenses(result, cat_data )
        

        elif switch == '5':
            month=int(input("Enter the month for the summary (1-12): "))
            monthly_summary(month, result)
            
        elif switch == '6':
            print("Exiting the program.")
            break
main()