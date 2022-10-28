import pandas as pd
from sqlalchemy import create_engine
import geocoder

# BLOQUE 1: HACEMOS LA CONEXION CON LOS DATOS REUTILIZADOS GUARDADOS EN EL ARCHIVO datosusuario.csv
#abrimos la info de datosusuario.csv y la guardamos en una lista
#importamos
df_data = pd.read_csv('datos_usuario.csv', delimiter=',', encoding='utf-8')
list_var = list(df_data['Variables'])

# traemos los elementos de la lista a las variables pertenecientes
usuario_var = list_var[0]
password_var = list_var[1]
host_var = list_var[2]
bd_var = list_var[3]
tabla_cliente_var = list_var[4]
tabla_localidad_var = list_var[5]
tabla_provincia_var = list_var[6]
tabla_pais_var = list_var[7]
campo_idcliente_var = list_var[8]
campo_idlocalidad_var = list_var[9]
campo_idprovincia_var = list_var[10]
campo_idpais_var = list_var[11]
campo_domicilio_var = list_var[12]
campo_localidad_var = list_var[13]
campo_provincia_var = list_var[14]
campo_pais_var = list_var[15]

#conexion
engine_concatenado = 'mysql://'+usuario_var+':'+password_var+'@'+host_var+'/'+bd_var
engine = create_engine(engine_concatenado)

# BLOQUE 2: HACEMOS LA COMPARACION ENTRE LA TABLA NUEVA Y LA TABLA VIEJA
#-------------------------------------------------------------------------------------------------------------

#LA TABLA VIEJA ESTA EN EL CSV CON LO CUAL SOLO LA LEVANTO
df_tabla_vieja = pd.read_csv('TablaVieja.csv', delimiter=',', encoding='utf-8')

#LA TABLA NUEVA ES UNA CONSULTA A LA BASE DE DATOS
#LA QUERY ES VARIABLE DEPENDIENDO DEL USUARIO. CON LO CUAL, DEBO TRAERME LOS DATOS GUARDADOS EN datos_usuario.csv

#query concatenada
query_concat = "SELECT " + campo_idcliente_var +', '+ campo_domicilio_var +', '+ campo_localidad_var +', '+ campo_provincia_var +', '+ campo_pais_var + " from " + tabla_cliente_var + " c join " + tabla_localidad_var + " l on  (c." + campo_idlocalidad_var + " = l." + campo_idlocalidad_var + ") join " + tabla_provincia_var + " pr on (pr." + campo_idprovincia_var + " = l." + campo_idprovincia_var + ") join " + tabla_pais_var + " pa on (pa." + campo_idpais_var +" = pr." + campo_idpais_var +");"

df_tabla_nueva = pd.read_sql_query(query_concat, engine)

#agregamos el domicilio completa para
df['domicilio_completo'] = df[campo_domicilio_var] + ', ' + df[campo_localidad_var] + ', ' +  df[campo_provincia_var] + ', ' + df[campo_pais_var]
print(df_tabla_vieja)
lista1 = list(df_tabla_vieja['domicilio_completo'])
lista2 = list(df_tabla_nueva['domicilio_completo'])
#comparamos la columna domicilio completo de la nueva con la vieja de l
if lista1 == lista2:
        print("las tablas no cambiaron")
        pass
else:
        print("las tablas no son iguales")
        def latitud(domicilio_completo):
                location = geocoder.osm(domicilio_completo)
                return location.lat


        def longitud(domicilio_completo):
                location = geocoder.osm(domicilio_completo)
                return location.lng   
        
        df_tabla_nueva['LatCliente'] = df_tabla_nueva['domicilio_completo'].apply(latitud)

        df_tabla_nueva['LongCliente'] = df_tabla_nueva['domicilio_completo'].apply(longitud)

        #se eliminan las columnas inecesarias
        df.drop(columns=[campo_domicilio_var, campo_localidad_var, campo_provincia_var, campo_pais_var], inplace = True)
        #actualiza la tabla bi_clientes_geo
        df_tabla_nueva.to_sql('bi_clientes_geo', con = engine, if_exists = 'replace')
        #esta tabla, pasa a ser la nueva de referencia
        df_tabla_nueva.to_csv('TablaVieja.csv')
