'''Задача 44: В ячейке ниже представлен код генерирующий DataFrame,
которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Надо это сделать без get_dummieНs.'''

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import pandas as pd #импорт библиотек
df = pd.DataFrame({'column': ['a', 'b', 'c','a', 'b', 'c', 'a']})  #создание DataFrame
unique_values = df['column'].unique() #получение уникальных значений столбца
one_hot_df = pd.DataFrame(0, index=df.index, columns=unique_values) #создание нового DataFrame с нулевым значением
for value in unique_values: #перебор уникальных значений и установка 1 в соответствующий столбец
one_hot_df.loc[df['column'] == value, value] = 1
print(one_hot_df)
