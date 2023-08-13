import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

data = pd.read_json('dados_compras.json')

data_list = data.to_dict(orient='records')

total_sales = 0
total_sales_value = 0
most_expensive = 0
less_expensive = float('inf')
men = 0
men_expenses = 0
women = 0
women_expenses = 0

for item in data_list:
    print(item)
    total_sales += data_list[0]['Valor']
    total_sales_value += item['Valor']
    if(item['Valor'] > most_expensive):
        most_expensive = item['Valor']
        most_expensive_item = item['Nome do Item']
    if (item['Valor'] < less_expensive):
        less_expensive = item['Valor']
        less_expensive_item = item['Nome do Item']
    if(item['Sexo'] == "Masculino"):
        men += 1
        men_expenses += item['Valor']
    else:
        women += 1
        women_expenses += item['Valor']

total_sales_average = total_sales_value / len(data_list)

#Exploração dos Dados
print(f'Quantidade de compras: {len(data_list)}')

#Análise de Compras
print(f'Valor médio gasto: {round(total_sales_average, 2)}')
print(f'Valor mínimo gasto: {less_expensive}')
print(f'Valor máximo gasto: {most_expensive}')
print(f'Produto mais barato: {less_expensive_item}')
print(f'Produto mais caro: {most_expensive_item}')

#Segmentação por Genêro
print(f'Homens: {men}')
print(f'    Gastos: {round(men_expenses, 2)}')
print(f'Mulheres: {women}')
print(f'Gastos: {round(women_expenses, 2)}')

#Visualização de Dados

# 1
data = {'Valor médio\n gasto': round(total_sales_average, 2), 'Valor mínimo\n gasto': less_expensive,
        'Valor máximo\n gasto': most_expensive}

courses = list(data.keys())
values = list(data.values())

items = [
    f'{round(total_sales_average, 2)}\n|',
    f'Item: {less_expensive_item}\n\n{less_expensive}\n|',
    f'Item: {most_expensive_item}\n\n{most_expensive}\n|'
]
fig = plt.figure(figsize=(10, 6), num='Página 1/2')
plt.bar(courses, values, color='maroon', width=0.4)
for courses, values, p in zip(courses, values, items):
    plt.text(courses, values, p, ha='center', va='bottom')

plt.xlabel(f'QUANTIDADE DE COMPRAS: {len(data_list)}')
plt.ylabel('Valor')
plt.title("Análise de Compras")
plt.show()

# 2
categories = ('Clientes', 'Gastos totais')
data = {
    'Homens': np.array([men, round(men_expenses, 2)]),
    'Mulheres': np.array([women, round(women_expenses, 2)])
    }

width = 0.6
fig, ax = plt.subplots(num='Página 2/2', )
bottom = np.zeros(2)
for sex, sex_count in data.items():
    p = ax.bar(categories, sex_count, width, label=sex, bottom=bottom)
    bottom += sex_count
    ax.bar_label(p, label_type='center')

men_color = (31/255, 119/255, 180/255)
women_color = (255/255, 127/255, 14/255)

female_patch = mpatches.Patch(color=men_color, label='Homens')
male_patch = mpatches.Patch(color=women_color, label='Mulheres')
plt.legend(handles=[female_patch, male_patch], loc='upper left', framealpha=0.5, frameon=True)

plt.xlabel(f'QUANTIDADE DE COMPRAS: {len(data_list)}')
plt.title('Segmentação por Genêro')
plt.show()
