def get_full_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# passing a list as an argument

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

""" preventing a function from modifying a list """

def print_models(unprinted, printed):
    """
    Simulate printing each design, until none are left.
    Move each design to printed after printing.
    """
    while unprinted:
        current_design = unprinted.pop()
        # Simulate creating a 3D print from the design.
        print(f"Printing model: {current_design}")
        printed.append(current_design)


# Collecting an arbitrary number of arguments

def make_pizza(size, *toppings):    # * means arbitrary number of arguments
    # Make a pizza with the given size and toppings.
    print(f"\nMaking a {size}-inch pizza with the following toppings:")

    for topping in toppings:
        print(f"- {topping}")


# Collecting an arbitrary number of keyword arguments
def build_profile(first, last, **user_info):
    # Build a dictionary containing everything we know about a user.
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics', age=25)
# print(user_profile)

if __name__ == "__main__":
    
    original = ['iphone case', 'robot pendant', 'dodecahedron']
    printed = []
    print_models(original, printed)
    print("\nOriginal designs:", original)
    print("Printed models:", printed)



    make_pizza('small', 'pepperoni')
    make_pizza('medium', 'mushrooms', 'green peppers', 'extra cheese')
    make_pizza('large', 'pepperoni', 'sausage', 'onions', 'green peppers', 'extra cheese')
