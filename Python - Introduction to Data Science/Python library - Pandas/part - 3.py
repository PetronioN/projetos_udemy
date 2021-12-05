import pandas as pd

food1 = {'number': [1, 2, 3, 4, 5], 'name': ['corn', 'banana', 'pizza', 'chips', 'popcorn'],
         'price': [2, 3, 4, 5, 6]}
food2 = {'number': [1, 2, 3, 4, 5], 'name': ['apple', 'banana', 'pizza', 'chips', 'popcorn'],
         'price': [2, 3, 4, 5, 6]}

table1 = pd.DataFrame(food1)
table2 = pd.DataFrame(food2)

fusion = pd.merge(table1, table2)

print(fusion)  # Fundiou as tabelas por conta do método merge.
# O nome apple nem corn foram printados porque eles são diferentes

print("")
fusionAlter = pd.merge(table1, table2, on="number")
print(fusionAlter)
# Da maneira acima, eu vou me importar somente com os números que estão iguais
"""Por mais que os outros valores estejam diferentes, se os numbers forem iguais, 
os outros valores serão printados da mesma maneira."""
