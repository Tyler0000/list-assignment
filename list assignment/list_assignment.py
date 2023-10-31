menu = {
    "Pizza": 7.30,
    "Pie": 3.45,
    "Burger": 4.50,
    "Chips": 2.00,
    "Onion rings": 2.30,
    "Drink": 1.50
}

order = []

total_cost = 0.0

print("Welcome to the Food Ordering Program!")

while True:
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: £{price:.2f}")
    
    choice = input("What would you like to order? (Type 'finish' to complete your order): ").capitalize()
    
    if choice == 'Finish':
      
        if len(order) > 0:
            print("\nYour Order:")
            for item in order:
                print(item)
            print(f"Total Cost: £{total_cost:.2f}")
        else:
            print("You haven't ordered anything.")
        break
    
    if choice in menu:
        order.append(choice)
        total_cost += menu[choice]
        print(f"{choice} added to your order. Current total: £{total_cost:.2f}")
    else:
        print("Invalid choice. Please select an item from the menu.")
