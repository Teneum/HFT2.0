from misc import *
from prettytable import PrettyTable
from databaseFunc import *
from plotting import *

initialize()
print("-----WELCOME TO HOME FINANCE TRACKER-----")
print("Helping you keep your expenses and spending in check")
view_general_menu()

while True:
    choice = input("Enter choice: ")
    if choice == '0':
        print("Thank you for using HFT. Goodbye.")
        break

    elif choice == '1':
        table = PrettyTable()
        table.field_names = ["ID", "Item", "Category", "Total Price", "Amount", "Date of Purchase"]

        view_item_menu()

        while True:
            menu_choice = input("Enter menu choice: ")

            if menu_choice == '1':
                itemname = input("Enter item name: ")
                data = get_item_data(itemname=itemname)
                for i in data:
                    table.add_row(i.values())
                break

            elif menu_choice == '2':
                data = get_all_item_data()
                for i in data:
                    table.add_row(i.values())
                break

            elif menu_choice == '3':
                sql = input("Please enter custom sql query: ")
                data = custom_sql(sql)
                for i in data:
                    table.field_names = i.keys()
                    table.add_rows(i)
                break

            else:
                print("Invalid choice")

        print("------------------")
        print(table)
        print("------------------")

    elif choice == '2':
        name = input("Enter item name: ").strip()
        category = input("Enter item category: ").strip()
        price = float(input("Enter item price: "))
        amount = float(input("Enter amount of item bought: "))
        dateofpurchase = input("Enter Date of Purchase(YYYY/MM/DD): ").strip()
        add_item_data(itemname=name, itemcategory=category, itemprice=price, itemamount=amount, dateofpurchase=dateofpurchase)

    elif choice == '3':
        id = int(input("Enter item id: "))
        delete_item_data(itemid=id)

    elif choice == '4':
        view_plot_menu()
        use_plot_menu()

    else:
        print("Invalid choice. Try again")