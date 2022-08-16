from prettytable import PrettyTable  # This is a class

table = PrettyTable()
table.add_column("Pokemon name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Area", ['Electric', 'Water', 'Fire'])
table.align = "l"

print(table)
