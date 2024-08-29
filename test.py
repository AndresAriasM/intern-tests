import pandas as pd
import re

def clean_dataframe(df):
    for col in df.columns:
        df[col] = df[col].str.strip()  # Elimina espacios en blanco

        df[col] = re.sub(r'\W+', '', df[col])

        df[col].fillna('', inplace=True) # Reemplaza NaN con cadena vacía
    
    return df

""" 
De entrada vemos que la función original maneja correctamente la eliminación 
de nulos. Para espacios en blanco falta una verificación del tipo de dato de la columna, que para el caso no cumple la
condición de ser de tipo cadena (string). Para ellos se implementa un condicional if que verifica el tipo de dato de la columna 
para hacer la respectiva correción. 

Nombre --> object
Edad --> float64

La columna 'Nombre' se convirtió a tipo string para ejecutar la función strip() y re.sub().
La columna 'Edad' se convirtió a tipo entero con soporte para nulos (Int64), garantizando calidad en los datos y los 
requisitos solicitados.

El segundo error observado se ecncuentra en la función re.sub se está aplicando a toda la serie de Pandas, lo que 
no es válido. Para ello, debemos usar apply() para aplicar re.sub a cada valor individual dentro de la columna.

.apply(lambda x: re.sub(r'\W+', '', x)) 

Importante recordar que la columna debe ser de tipo string, de lo contrario marcará error.
"""

def clean_dataframe_solution(df):
    for col in df.columns:
        if df[col].dtype == 'object':  # Verificación implementada para corregir el tipo de dato de la columna
            df[col] = df[col].astype(str)  # Convierte la columna a tipo string 
            df[col] = df[col].str.strip() 
            df[col] = df[col].apply(lambda x: re.sub(r'\W+', '', x))  # Elimina caracteres no alfanuméricos aplicado a cada valor individual de la columna
            df[col].fillna('', inplace=True)
        elif df[col].dtype == 'float64': # Verificación implementada para corregir el tipo de dato de la columna
            df[col] = df[col].astype('Int64')  # Convierte la columna a tipo int con soporte para nulos
    return df

#Cargar los datos desde el path dentro del proyecto
data = pd.read_csv("data/interns.csv", sep=',') 
#print(data.head())
#print(data.dtypes)

# Ejecutar la función de limpieza con las modificaciones realizadas
cleaned_data = clean_dataframe_solution(data)

# Guardar el nuevo dataframe con los datos limpios
cleaned_data.to_excel("respuestas/andresariasmedina_test1.xlsx", index=False, engine='openpyxl')
print(cleaned_data.head())
