# Rules the user must follow throughout the entire program
def get_float_input(prompt):
    """Helper function to get a non-negative float input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

# Rules the user must follow when entering number of attendees
def get_num_people():
    """Helper function to get the number of people attending, with a minimum of 3 and a maximum of 300."""
    while True:
        try:
            num_people = int(input("Enter the number of people attending the party (minimum 3, maximum 300): "))
            if num_people < 3:
                print("Please enter a number that is at least 3.")
            elif num_people > 300:
                print("Please enter a number that is 300 or less.")
            else:
                return num_people
        except ValueError:
            print("Invalid input. Please enter a valid number of people.")


def get_party_details():
    """Gather details about the party and return the data."""
    # Get the number of people attending
    num_people = get_num_people()

    # Initialize lists to store food and drink details
    food_items = []
    drink_items = []

    # Get food items
    print("Enter details for food items (type 'done' when finished):")
    while True:
        food_name = input("Food item name: ").strip()
        if food_name.lower() == 'done':
            break
        cost_per_unit = get_float_input(f"Cost per {food_name}: ")
        quantity_per_person = get_float_input(f"Quantity of {food_name} per person: ")
        food_items.append({'name': food_name, 'cost_per_unit': cost_per_unit, 'quantity_per_person': quantity_per_person})

    # Get drink items
    print("Enter details for drink items (type 'done' when finished):")
    while True:
        drink_name = input("Drink item name: ").strip()
        if drink_name.lower() == 'done':
            break
        cost_per_unit = get_float_input(f"Cost per {drink_name}: ")
        quantity_per_person = get_float_input(f"Quantity of {drink_name} per person: ")
        drink_items.append({'name': drink_name, 'cost_per_unit': cost_per_unit, 'quantity_per_person': quantity_per_person})

    # Summary of items entered
    print(f"\nTotal food items entered: {len(food_items)}")
    print(f"Total drink items entered: {len(drink_items)}")

    return num_people, food_items, drink_items

# Calculations
def calculate_totals(num_people, food_items, drink_items):
    """Calculate total quantities and costs for food and drinks."""
    total_cost = 0
    totals = {'food': [], 'drink': []}

    # Calculate totals for food
    for item in food_items:
        total_quantity = item['quantity_per_person'] * num_people
        total_cost += total_quantity * item['cost_per_unit']
        totals['food'].append({'name': item['name'], 'quantity': total_quantity, 'cost': total_quantity * item['cost_per_unit']})

    # Calculate totals for drinks
    for item in drink_items:
        total_quantity = item['quantity_per_person'] * num_people
        total_cost += total_quantity * item['cost_per_unit']
        totals['drink'].append({'name': item['name'], 'quantity': total_quantity, 'cost': total_quantity * item['cost_per_unit']})

    return totals, total_cost


# Gives user the instructions
def instructions():
    """Display instructions for using the program."""
    print("\n******** Instructions ********")
    print()
    print("This program helps you plan and budget for a party by calculating")
    print("the total quantity and cost of food and drinks based on the number")
    print("of people attending.")
    print()
    print("First, you'll be asked to enter the number of people attending.")
    print("Then, you'll input details for each food and drink item, including")
    print("the cost per unit and the quantity needed per person.")
    print()
    print("After entering all items, the program will calculate the total")
    print("quantity and cost for each item, and provide a summary of the")
    print("total costs for the party.")
    print()
    print("Please ensure that you enter valid numeric values for costs and")
    print("quantities. Type 'done' when you have finished entering items.")
    print()
    print("Please make sure that you enter FOOD items FIRST")
    print()
    print("Please make sure that you enter DRINK items SECOND")
    print()
    print("**********")
    print()

# Welcomes the user to the program
def main():
    print("******** Welcome to the Party Planner ********")
    print()
    
    # Displays instructions
    instructions()
    
    num_people, food_items, drink_items = get_party_details()
    totals, total_cost = calculate_totals(num_people, food_items, drink_items)

    print("\nSummary of Items and Costs:")
    print("\nFood Items:")
    for item in totals['food']:
        print(f"{item['name']}: {item['quantity']} units, Total Cost: ${item['cost']:.2f}")

    print("\nDrink Items:")
    for item in totals['drink']:
        print(f"{item['name']}: {item['quantity']} units, Total Cost: ${item['cost']:.2f}")

    print(f"\nTotal Cost for the Party: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
