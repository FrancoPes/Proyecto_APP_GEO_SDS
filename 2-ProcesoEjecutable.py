import pandas as pd
from sqlalchemy import create_engine
import geocoder

# hacemos la conexion
engine = create_engine('mysql://root:matias1997@localhost/prueba_python')

df_tabla_vieja = pd.read_csv('TablaVieja.csv', delimiter=',', encoding='utf-8')
df_tabla_nueva = pd.read_sql_query("select ID, Domicilio, Localidad, Provincia from clientes limit 10", engine)

#agregamos el domicilio completa para
df_tabla_nueva['domicilio_completo'] = df_tabla_nueva['Domicilio'] + ', ' + df_tabla_nueva['Localidad']
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

        #dropeamos tablas innecesarias 
        df.drop(columns=['Domicilio', 'Localidad', 'Provincia'], inplace = True)
        #actualiza la tabla bi_clientes_geo
        df_tabla_nueva.to_sql('bi_clientes_geo', con = engine, if_exists = 'replace')
        #esta tabla, pasa a ser la nueva de referencia
        df_tabla_nueva.to_csv('TablaVieja.csv')
