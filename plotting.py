import matplotlib.pyplot as plt
from databaseFunc import *

def use_plot_menu():
    print("------------------")
    choice = input("Enter plot-menu choice: ")

    if choice == "0":
        print("------------------")
        pass

    elif choice == "1":
        graph_spending_for_all_category()
        use_plot_menu()

    elif choice == "2":
        cat = input("Enter category: ")
        graph_spending_by_category(cat)
        use_plot_menu()

    elif choice == "3":
        graph_amount_for_all_category()
        use_plot_menu()

    elif choice == "4":
        cat = input("Enter category: ")
        graph_amount_by_category(cat)
        use_plot_menu()

    else:
        print("Invalid input")
        use_plot_menu()


def graph_spending_for_all_category():
    data = get_all_item_data()
    formatted_data = {}

    for i in data:
        if i['Category'] not in formatted_data:
            formatted_data[i['Category']] = i['Price']
        else:
            formatted_data[i['Category']] += i['Price']

    categories = list(formatted_data.keys())
    values = list(formatted_data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(categories, values, color='maroon',
            width=0.4)

    plt.xlabel("Categories")
    plt.ylabel("Money spent")
    plt.title("Money spent per category")
    plt.show()

def graph_spending_by_category(category):
    data = get_item_data_by_category(category=category)
    formatted_data = {}

    for i in data:
        if i['Name'] not in formatted_data:
            formatted_data[i['Name']] = i['Price']
        else:
            formatted_data[i['Name']] += i['Price']

    categories = list(formatted_data.keys())
    values = list(formatted_data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(categories, values, color='maroon',
            width=0.4)

    plt.xlabel("Items")
    plt.ylabel("Money spent")
    plt.title(f"Money spent per item in category {category}")
    plt.show()

def graph_amount_by_category(category):
    data = get_item_data_by_category(category=category)
    formatted_data = {}

    for i in data:
        if i['Name'] not in formatted_data:
            formatted_data[i['Name']] = i['Amount']
        else:
            formatted_data[i['Name']] += i['Amount']

    categories = list(formatted_data.keys())
    values = list(formatted_data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(categories, values, color='maroon',
            width=0.4)

    plt.xlabel("Items")
    plt.ylabel("Amount")
    plt.title(f"Amount bought per item in category {category}")
    plt.show()

def graph_amount_for_all_category():
    data = get_all_item_data()
    formatted_data = {}

    for i in data:
        if i['Category'] not in formatted_data:
            formatted_data[i['Category']] = i['Amount']
        else:
            formatted_data[i['Category']] += i['Amount']

    categories = list(formatted_data.keys())
    values = list(formatted_data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(categories, values, color='maroon',
            width=0.4)

    plt.xlabel("Categories")
    plt.ylabel("Amount bought")
    plt.title("Amount bought per category")
    plt.show()

