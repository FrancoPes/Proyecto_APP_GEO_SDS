import pandas as pd
from sqlalchemy import create_engine
import geocoder
#este archivo se ejecuta una sola vez
# hacemos la conexion
                        #TipoBD_//usuario://password@localhost/baseDatos

engine = create_engine('mysql://root:matias1997@localhost/prueba_python')

# hacemos el dataframe a partir de una consulta a la base 
df = pd.read_sql_query("select ID, Domicilio, Localidad, Provincia from clientes limit 10", engine)
df['domicilio_completo'] = df['Domicilio'] + ', ' + df['Localidad'] + ', ' +  df['Provincia']
    #creamos las funciones 
def latitud(domicilio_completo):
        location = geocoder.osm(domicilio_completo)
        return location.lat


def longitud(domicilio_completo):
        location = geocoder.osm(domicilio_completo)
        return location.lng

#mapeamos el comicilio del cliente
df['LatCliente'] = df['domicilio_completo'].apply(latitud)

df['LongCliente'] = df['domicilio_completo'].apply(longitud)

#sacar columnas innecesarias
df.drop(columns=['Domicilio', 'Localidad', 'Provincia'], inplace = True)

print(df)

#mandamos la tabla mapeada a la base, la cual se llama bi_clientes_geo
df.to_sql('bi_clientes_geo', con = engine, if_exists = 'replace')

#guarda en un to_csv#para luego comparar
df.to_csv('TablaVieja.csv', index = False)
print("Instalación ejecutada con exito!")
