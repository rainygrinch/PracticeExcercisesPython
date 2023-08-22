def welcome():
    print("Hello, welcome to the RainyGrinch coffee shop!")
    username = input("What is your name?: ")
    print("Hello " + username + ", thank you so much for coming in today!")
    print("Here is a list of available products, what would you like to order?")
    print("**MENU**")
    print("1. Coffees")
    print("2. Teas")
    print("3. Cakes")
    print("4. Done Ordering")  # Added an option to indicate when the user is done ordering


def choice():
    choice = input("Please make a selection from the menu:")
    if choice == "1":
        coffee_cost = order_items("coffee")  # Call the 'order_items' function for coffee selection
        return coffee_cost
    elif choice == "2":
        tea_cost = order_items("tea")  # Call the 'order_items' function for tea selection
        return tea_cost
    elif choice == "3":
        cake_cost = order_items("cake")  # Call the 'order_items' function for cake selection
        return cake_cost
    elif choice == "4":
        print("Thank you for your order!")
        return 0  # Return 0 to indicate the user is done ordering
    else:
        print("I'm sorry, I don't recognize that answer, please select from the menu items by entering\n"
              "the corresponding number:")
        return choice()


def order_items(item_type):
    total_cost = 0.0
    while True:
        print(f"Which type of {item_type} would you like to order?")
        if item_type == "coffee":
            print("1. Espresso - £2.50")
            print("2. Cappuccino - £3.00")
            print("3. Latte - £3.50")
        elif item_type == "tea":
            print("1. Green Tea - £2.00")
            print("2. Black Tea - £2.00")
            print("3. Herbal Tea - £2.50")
        elif item_type == "cake":
            print("1. Chocolate Cake - £4.00")
            print("2. Carrot Cake - £4.50")
            print("3. Cheesecake - £5.00")

        item_choice = input("Please enter the number of your choice or '0' to stop ordering this item:")

        if item_choice == "0":
            break  # Exit the loop if the user is done ordering this item
        elif item_choice in ["1", "2", "3"]:
            quantity = int(input(f"How many {item_type}s would you like to order?"))
            if item_type == "coffee":
                cost_per_item = get_coffee_cost(item_choice)
            elif item_type == "tea":
                cost_per_item = get_tea_cost(item_choice)
            elif item_type == "cake":
                cost_per_item = get_cake_cost(item_choice)

            total_cost += (cost_per_item * quantity)

    return total_cost


def get_coffee_cost(coffee_choice):
    if coffee_choice == "1":
        return 2.50
    elif coffee_choice == "2":
        return 3.00
    elif coffee_choice == "3":
        return 3.50


def get_tea_cost(tea_choice):
    if tea_choice == "1":
        return 2.00
    elif tea_choice == "2":
        return 2.00
    elif tea_choice == "3":
        return 2.50


def get_cake_cost(cake_choice):
    if cake_choice == "1":
        return 4.00
    elif cake_choice == "2":
        return 4.50
    elif cake_choice == "3":
        return 5.00


def main():
    total_cost = 0.0
    welcome()

    while True:
        item_cost = choice()
        if item_cost == 0:
            break  # Exit the loop if the user is done ordering
        total_cost += item_cost

    print(f"Your total cost is £{total_cost:.2f}. Enjoy your meal!")


if __name__ == "__main__":
    main()
