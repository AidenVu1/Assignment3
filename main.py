LARGE_PIZZA_COST = 6.00
XL_PIZZA_COST = 10.00

ONE_TOPPING_COST = 1.00
TWO_TOPPINGS_COST = 1.75
THREE_TOPPINGS_COST = 2.50
FOUR_TOPPINGS_COST = 3.35

HST_RATE = 0.13

pizza_size = input("Enter 'L' for large pizza or 'XL' for extra large pizza: ")

if pizza_size == "L":
    pizza_cost = LARGE_PIZZA_COST
elif pizza_size == "XL":
    pizza_cost = XL_PIZZA_COST
else:
    print("Invalid pizza size")
    exit()

while True:
    try:
        num_toppings = int(input("Enter the number of toppings (1-4): "))
        if num_toppings >= 1 and num_toppings <= 4:
            break
        else:
            print("Invalid number of toppings, please try again.")
    except ValueError:
        print("Invalid input, please enter a number between 1 and 4.")

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

subtotal = pizza_cost + (num_toppings * toppings_cost)
tax = subtotal * HST_RATE

total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")