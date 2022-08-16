from data import MENU, resources


def use_resources(menu, resource, order):
    for key in resource:
        resource[key] = resource[key] - menu[order]["ingredients"][key]
        if resource[key] < 0:
            return False
    return resource


def take_money(amount, menu, order):
    extra_change = amount - menu[order]['cost']
    return extra_change


def coffee_machine():
    order_coffee = True
    remaining_resources = resources
    while order_coffee:
        order = input("What would you like to have (espresso, latte, cappuccino)?")
        if order == 'report':
            print(remaining_resources)
        elif order == 'no':
            return
        amount = int(input('Enter amount'))
        extra_change = take_money(amount, MENU, order)

        if extra_change < 0:
            print(f'You need to enter {-extra_change} more dollars')
        else:
            remaining_resources = use_resources(resource=remaining_resources, order=order, menu=MENU)
            if not remaining_resources:
                print("Sorry, resources are not present")
                return
            else:
                print(f'Here is your coffee, and change = {extra_change}')


coffee_machine()
