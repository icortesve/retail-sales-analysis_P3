import pandas as pd

def cargar_datos(ruta_archivo):
    # Cargar los datos del archivo CSV utilizando NumPy
    # Se utiliza dtype=None para identificar texto y números automáticamente
    # encoding='utf-8' para evitar errores de lectura en caracteres especiales
    datos = pd.read_csv(ruta_archivo)
    return datos

def categorizar_ventas(monto):

    if monto > 1000:
        return 'Alta'
    elif monto > 100:
        return 'Media'
    else:
        return 'Baja'

def clasificar_ventas(df):

    # Categorizar_monto a cada fila de la columna 'Ingreso total'
    df['Categoria Venta'] = df['Ingreso Total'].apply(categorizar_ventas)
    
    return df