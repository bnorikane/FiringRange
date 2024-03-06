# Dead Simple Python - Structural Pattern Matching

lunch_order = input('What would you like for lunch? ')

match lunch_order:
    case 'pizza':
        print('Pizza time!')
    case 'sandwich':
        print("Here's your sandwich")
    case 'taco':
        print('Taco, taco, TACO, tacotacotaco!')
    case 'salad' | 'soup':  # logical or 
        print('Eating healthy, eh?')
    case order:  # assigns lunch_order to order. acts as wildcard, matches anything, 
        print(f"Enjoy your {order}.")

    # case _:  # wildcard matches anything
    #     print('Yummy.')
