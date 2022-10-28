import pandas as pd
from sqlalchemy import create_engine

#variables 
usuario_var = input(f"Introduzca el usuario de la Base de datos: ")
password_var = input(f"Introduzca la contraseña: ")
host_var = input(f"Introduzca el host: ")
bd_var = input(f"Introduzca el nombre de la base de datos: ")
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
# Lists you want to convert to a Pandas dataframe
lista_variables = [usuario_var, password_var, host_var, bd_var, tabla_cliente_var, tabla_localidad_var, tabla_provincia_var, tabla_pais_var, campo_idlocalidad_var, campo_idprovincia_var, campo_idpais_var, campo_domicilio_var, campo_localidad_var, campo_provincia_var, campo_pais_var]


# Make dictionary, keys will become dataframe column names
diccionario_data = {'Variables':lista_variables}

# Convert dictionary to Pandas dataframe
df_data = pd.DataFrame(diccionario_data)

print(df_data)