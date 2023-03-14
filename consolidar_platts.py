import os
import shutil
import glob
import pandas as pd

# Ruta de la carpeta de origen y destino
ruta_origen = r'C:\Users\Fernando\Desktop\PLATTS_full'
ruta_destino = r'C:\Users\Fernando\Desktop\archivos_csv'

# Obtener la lista de archivos CSV en la carpeta de origen
archivos_csv = [f for f in os.listdir(ruta_origen) if f.endswith('.csv')]

# Mover cada archivo CSV a la carpeta de destino
for archivo_csv in archivos_csv:
    ruta_archivo = os.path.join(ruta_origen, archivo_csv)
    shutil.move(ruta_archivo, ruta_destino)

# Lista de todos los archivos CSV en la carpeta de destino
csv_files = glob.glob(os.path.join(ruta_destino, "*.csv"))

# Guarda el DataFrame combinado como un archivo CSV
df = pd.concat((pd.read_csv(f) for f in csv_files))

df.to_csv(os.path.join(ruta_destino, "consolidado_platts.csv"), index=False)