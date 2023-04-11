# Define the cost of each pizza size
LARGE_PIZZA_COST = 6.00
XL_PIZZA_COST = 10.00

# Define the cost of each topping option
ONE_TOPPING_COST = 1.00
TWO_TOPPINGS_COST = 1.75
THREE_TOPPINGS_COST = 2.50
FOUR_TOPPINGS_COST = 3.35

# Define the tax rate
HST_RATE = 0.13

# Prompt the user for pizza size
pizza_size = input("Enter 'L' for large pizza or 'XL' for extra large pizza: ")

# Prompt the user for the number of toppings
num_toppings = int(input("Enter the number of toppings (1-4): "))

# Calculate the pizza cost based on size
if pizza_size == "L":
    pizza_cost = LARGE_PIZZA_COST
elif pizza_size == "XL":
    pizza_cost = XL_PIZZA_COST
else:
    print("Invalid pizza size")
    exit()

# Calculate the cost of toppings based on number
if num_toppings == 1:
    toppings_cost = ONE_TOPPING_COST
elif num_toppings == 2:
    toppings_cost = TWO_TOPPINGS_COST
elif num_toppings == 3:
    toppings_cost = THREE_TOPPINGS_COST
elif num_toppings == 4:
    toppings_cost = FOUR_TOPPINGS_COST
else:
    print("Invalid number of toppings")
    exit()

# Calculate the subtotal and tax
subtotal = pizza_cost + (num_toppings * toppings_cost)
tax = subtotal * HST_RATE

# Calculate the total cost
total = subtotal + tax

# Display the results
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
