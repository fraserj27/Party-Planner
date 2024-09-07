def get_float_input(prompt):
    """Helper function to get a float input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")



def get_party_details():
    """Gather details about the party and return the data."""
    # Get the number of people attending
    num_people = int(get_float_input("Enter the number of people attending the party: "))

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

    return num_people, food_items, drink_items



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



def main():
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
