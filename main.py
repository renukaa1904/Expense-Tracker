# Expense Tracker

expenselist = [] # list of all expense form dictionary
print("Welcome To expense Tracker")
while True:
    print("=MEnu=")
    print("1.Add Expense")
    print("2.view All Expense")
    print("3.view Total Expense")
    print("4.Exit")

    choice= int(input("Please Enter Your Choice : "))
    # Add Expense
    if(choice ==1):
        date=input("on which date did i spend the money?: ")
        category=input("which type of expense? (Food,Makeup,Travel,Books):")
        description=input("add more details")
        amount=float(input("Enter The Amount"))

        expense={"date":date, "category":category,"description":description, "amount":amount }

        expenselist.append(expense)
        
        print( "\n Done Expense added successfully:")

     # View all expense
    if(choice ==2) :
        if(len (expenselist) ==0) :
            print("No Expense Added.First spend the money")
        else:
            print("This Your All Expense")   
            count=1
            for allspend in expenselist:
             print(f"Kharcha Number {count} -> {allspend["date"]}, {allspend["category"]}, {allspend["description"]}, {allspend["amount"]} ")
             count=count+1
    # view Total Spending   
    elif(choice ==3):
        total=0
        for allspend in expenselist:
            total= total+allspend["amount" ]
            print("\n total spend",total)
    #View Exit
    elif(choice ==4):
        print("Thanku for using Our System")
        break
    else:
        ("Invalid Choice. Try Again")






