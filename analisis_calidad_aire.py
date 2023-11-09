import pandas as pd
import requests
import sqlite3
from typing import Set

def ej_1_cargar_datos_demograficos() -> pd.DataFrame:
    url = "https://public.opendatasoft.com/explore/dataset/us-cities-demographics/download/?format=csv&timezone=Europe/Berlin&lang=en&use_labels_for_header=true&csv_separator=%3B"
    data = pd.read_csv(url, sep=';')
    return data

def ej_2_cargar_calidad_aire(ciudades: Set[str]) -> None:
    # Crear un DataFrame vacío para almacenar los resultados
    df = pd.DataFrame()

    for ciudad in ciudades:
        api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(ciudad)
        response = requests.get(api_url, headers={'X-Api-Key': 'qhxSfn5S79v19+eUbFSF0w==JuwyKcGBH3SEoRiG'})

        if response.status_code == requests.codes.ok:
            data = response.json()
            # Crear un diccionario para almacenar la ciudad y las concentraciones
            data_concentration = {'city': ciudad}
            for key in data:
                if isinstance(data[key], dict) and 'concentration' in data[key]:
                    # Guardar solo la concentración de cada contaminante
                    data_concentration[key] = data[key]['concentration']
            # Añadir los datos al DataFrame
            df = df._append(data_concentration, ignore_index=True)
        else:
            print("Error:", response.status_code, response.text)
    # Guardar el DataFrame en un archivo CSV
    df.to_csv('calidad_aire.csv', index=False)

nuevo_datos_demograficos = ej_1_cargar_datos_demograficos().drop(['Race', 'Count', 'Number of Veterans'], axis = 1)
nuevo_datos_demograficos = nuevo_datos_demograficos.drop_duplicates()
nuevo_datos_demograficos = nuevo_datos_demograficos.reset_index(drop=True)

ciudades = nuevo_datos_demograficos['City']

df_calidad_aire = pd.read_csv('calidad_aire.csv')

# Crear una conexión a la base de datos SQLite
conn = sqlite3.connect('analisis_calidad_aire.sqlite')

# Exportar el DataFrame a la base de datos SQLite
nuevo_datos_demograficos.to_sql('datos_demografico', conn, if_exists='replace', index=False)
df_calidad_aire.to_sql('calidad_aire', conn, if_exists='replace', index=False)
