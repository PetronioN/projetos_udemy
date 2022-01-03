import pandas as pd

Employee = {'number': [1, 2, 3, 4, 5], 'name': ['addy', 'john', 'lina', 'mark', 'bob'],
            'ourly salary': [15, 25, 52, 27, 48]}
table1 = pd.DataFrame(Employee)

print(table1.head(2))  #Mostra somente as 2 primeiras linhas da nossa lista

print(table1.tail(2))  #Gera as duas últimas linhas