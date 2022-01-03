import pandas as pd

food1 = {'number': [1, 2, 3, 4, 5], 'name': ['apple', 'banana', 'chips', 'popcorn', 'pizza'], 'price': [1, 2, 3, 4, 5]}
food2 = {'caller': ['red', 'yellow', 'orange', 'white', 'blue'], 'weight': [100, 200, 340, 175, 225],
         'qt': [1, 2, 1, 3, 4]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

fusion = table1.join(table2)
# O fusion acima junta as duas tables em uma

print(fusion)
