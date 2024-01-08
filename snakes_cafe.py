print("""
    **************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************""")

total_order = []

def order():
    user_order = input("> ")
    while user_order.lower() != 'quit' and user_order.lower() != 'done':
        total_order.append(user_order)
        print("Ok! I have added one order of", user_order, "to your meal. Your order now includes ", total_order, ". Would you like to add anything else to your order? Enter 'done' any time to complete your order or 'quit' to exit and cancel your order.")
        user_order = input("> ")

    if user_order.lower() == 'quit':
        print("Thank you for visiting Snakes Cafe. Have a great day!")
    elif user_order.lower() == 'done':
        order_string = ', '.join(total_order)
        print("Thank you for visiting Snakes Cafe. Your final order is:", order_string, ". Have a great day!") 

order()
