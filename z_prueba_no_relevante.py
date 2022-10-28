import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql://root:root@localhost/prueba_python')
#Tablas
tabla_cliente_var = "cliente"
tabla_localidad_var = "localidad"
tabla_provincia_var = "provincia"
tabla_pais_var = "pais"
#campos
campo_idcliente_var = 'id_cliente'
campo_domicilio_var = 'domicilio'
campo_localidad_var = 'Localidad'
campo_provincia_var = 'Provincia'
campo_pais_var = 'Pais'
query_concat = "SELECT " + campo_idcliente_var +', '+ campo_domicilio_var +', '+ campo_localidad_var +', '+ campo_provincia_var +', '+ campo_pais_var + " from " + tabla_cliente_var + " c join " + tabla_localidad_var + " l on  (c.id_localidad = l.id_localidad) join " + tabla_provincia_var + " pr on (pr.id_provincia = l.id_provincia) join " + tabla_pais_var + " pa on (pa.id_pais = pr.id_pais);"
#df = pd.read_sql_query(query_concat, engine)
print(query_concat)