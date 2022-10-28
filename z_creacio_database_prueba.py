import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql://root:root@localhost/prueba_python')

df = pd.read_csv("clientes.csv", sep=";", encoding = 'utf-8')
df1 = pd.read_csv("localidad.csv", sep=";",encoding = 'utf-8')
df2 = pd.read_csv("Provincia.csv", sep=";",encoding = 'utf-8')
df3 = pd.read_csv("pais.csv", sep=";", encoding = 'utf-8')

df.to_sql('cliente', con = engine, if_exists = 'replace')
df1.to_sql('localidad', con = engine, if_exists = 'replace')
df2.to_sql('provincia', con = engine, if_exists = 'replace')
df3.to_sql('pais', con = engine, if_exists = 'replace')