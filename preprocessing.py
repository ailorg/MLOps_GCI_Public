import pandas as pd
import sqlite3

file = "sample.db"
conn = sqlite3.connect(file)

df_test = pd.read_sql_query('SELECT * FROM test', conn)

missing_list = ['Age', 'Fare', 'Cabin', 'Embarked']
df_test.drop(missing_list, axis=1, inplace=True)

category_list = ['Name', 'Sex', 'Ticket']
df_test.drop(category_list, axis=1, inplace=True)

df_test = df_test.iloc[:, 1:]
df_test.to_sql('feature', conn, if_exists='replace', index=True)
