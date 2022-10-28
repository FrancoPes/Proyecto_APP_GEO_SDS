import pandas as pd
from sqlalchemy import create_engine
import geocoder


#BLOQUE 1:INSERCION DE LOS DATOS PARA LA CONEXION CON MYSQL
usuario_var = input(f"Introduzca el usuario de la Base de datos: ")
password_var = input(f"Introduzca la contraseña: ")
host_var = input(f"Introduzca el host: ")
bd_var = input(f"Introduzca el nombre de la base de datos: ")

engine_concatenado = 'mysql://'+usuario_var+':'+password_var+'@'+host_var+'/'+bd_var
engine = create_engine(engine_concatenado)

##-----------------------------------------------------------------------------------------------------------------
#BLOQUE 2:INSERCION DE LOS DATOS DE SU BASE DE DATOS (TABLAS Y CAMPOS)
#Tablas
tabla_cliente_var = input(f"Por favor introduzca el nombre de su tabla clientes: ")
tabla_localidad_var = input(f"Por favor introduzca el nombre de su tabla Localidad/Zona: ")
tabla_provincia_var = input(f"Por favor introduzca el nombre de su tabla Provincia/Region: ")
tabla_pais_var = input(f"Por favor introduzca el nombre de su tabla Pais: ")
#campos
campo_idcliente_var = input(f"Por favor introduzca la primary key de su tabla {tabla_cliente_var}:")
campo_idlocalidad_var = input(f"Por favor introduzca la primary key de su tabla {tabla_localidad_var}:")
campo_idprovincia_var = input(f"Por favor introduzca la primary key de su tabla {tabla_provincia_var}:")
campo_idpais_var = input(f"Por favor introduzca la primary key de su tabla {tabla_pais_var}:")
campo_domicilio_var = input(f"Por favor introduzca el campo domicilio de su tabla {tabla_cliente_var}:")
campo_localidad_var = input(f"Por favor introduzca el campo localidad/Zona de su tabla {tabla_localidad_var}:")
campo_provincia_var = input(f"Por favor introduzca el campo provincia/Region de su tabla {tabla_provincia_var}:")
campo_pais_var = input(f"Por favor introduzca el campo Pais de su tabla {tabla_pais_var}:")

#query concatenada
query_concat = "SELECT " + campo_idcliente_var +', '+ campo_domicilio_var +', '+ campo_localidad_var +', '+ campo_provincia_var +', '+ campo_pais_var + " from " + tabla_cliente_var + " c join " + tabla_localidad_var + " l on  (c." + campo_idlocalidad_var + " = l." + campo_idlocalidad_var + ") join " + tabla_provincia_var + " pr on (pr." + campo_idprovincia_var + " = l." + campo_idprovincia_var + ") join " + tabla_pais_var + " pa on (pa." + campo_idpais_var +" = pr." + campo_idpais_var +");"


##-----------------------------------------------------------------------------------------------------------------
#BLOQUE 3: LECTURA DEL DATAFRAME Y GEOLOCALIZACION
df = pd.read_sql_query(query_concat, engine)   #SE GUARDA EN UN DATAFRAME

#se crea una nueva columna con el domicilio completo
df['domicilio_completo'] = df[campo_domicilio_var] + ', ' + df[campo_localidad_var] + ', ' +  df[campo_provincia_var] + ', ' + df[campo_pais_var]

#se eliminan las columnas inecesarias
df.drop(columns=[campo_domicilio_var, campo_localidad_var, campo_provincia_var, campo_pais_var], inplace = True)

#se crean las funciones de latitud y logitud
def latitud(domicilio_completo):
        location = geocoder.osm(domicilio_completo)
        return location.lat
def longitud(domicilio_completo):
        location = geocoder.osm(domicilio_completo)
        return location.lng

#se mapea el domicilio completo del cliente
df['LatCliente'] = df['domicilio_completo'].apply(latitud)
df['LongCliente'] = df['domicilio_completo'].apply(longitud)

#sacar columnas innecesarias
#df.drop(columns=[campo_domicilio_var, campo_localidad_var, campo_provincia_var, campo_pais_var], inplace = True)

print(df)
##-----------------------------------------------------------------------------------------------------------------
#BLOQUE 4: ENVIO DE DATOS DE LA TABLA PARA COMPARAR a un archivo
#mandamos la tabla mapeada a la base, la cual se llama bi_clientes_geo
df.to_sql('bi_clientes_geo', con = engine, if_exists = 'replace')

#guarda en un to_csv#para luego comparar
df.to_csv('TablaVieja.csv', index = False)



##-----------------------------------------------------------------------------------------------------------------
#BLOQUE 5: ENVIO DE DATOS DEL USUARIO A UN ARCHIVO PARA REUTILIZARLOS
lista_variables = [usuario_var, password_var, host_var, bd_var, tabla_cliente_var, tabla_localidad_var, tabla_provincia_var, tabla_pais_var, tabla_cliente_var, campo_idlocalidad_var, campo_idprovincia_var, campo_idpais_var, campo_domicilio_var, campo_localidad_var, campo_provincia_var, campo_pais_var]
diccionario_data = {'Variables':lista_variables}
#convertimos en un dataframe
df_data = pd.DataFrame(diccionario_data)
df_data.to_csv('datos_usuario.csv', index = False)

print("Instalación ejecutada con exito!")
