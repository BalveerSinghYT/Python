# Importing an entire module
# File: demo.py contain pizze function
# Every function is stored in a module. You can import an entire module and then use dot notation to access the functions you need from that module. For example, to use the function make_pizza() from the module pizza, we need to import the module pizza:


from demo import make_pizza as pizza  # as is an alias

pizza("large", "pepperoni", "sausage", "onions", "green peppers", "extra cheese")

# Importing specific functions

import demo

print(demo.build_profile("albert", "einstein", location="princeton", field="physics", age=25))
