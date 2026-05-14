import pandas as pd

def cargar_datos(ruta_archivo):
    """
    Carga un archivo CSV y lo convierte en un DataFrame de Pandas.
    
    Args:
        ruta_archivo (str): La ruta local donde se encuentra el dataset.
        
    Returns:
        DataFrame: Un objeto de Pandas con los datos cargados.
    """
    datos = pd.read_csv(ruta_archivo)
    return datos

def categorizar_ventas(monto):
    """
    Asigna una etiqueta de texto según el rango del monto de venta.
    
    Args:
        monto (float): El valor total de una venta individual.
        
    Returns:
        str: 'Alta', 'Media' o 'Baja' según el valor.
    """
    if monto > 1000:
        return 'Alta'
    elif monto > 100:
        return 'Media'
    else:
        return 'Baja'

def clasificar_ventas(df):
    """
    Aplica la categorización de ventas a todo el DataFrame.
    
    Args:
        df (DataFrame): El DataFrame original con la columna 'Ingreso Total'.
        
    Returns:
        DataFrame: El DataFrame con la nueva columna 'Categoria Venta' añadida.
    """
    # Categorizar_monto a cada fila de la columna 'Ingreso total'
    df['Categoria Venta'] = df['Ingreso Total'].apply(categorizar_ventas)
    
    return df

def calcular_desviacion(x):
    """
    Calcula la diferencia entre cada valor y el promedio de su grupo.
    
    Args:
        x (Series): Columna de datos numéricos.
        
    Returns:
        Series: Los valores restados por su media aritmética.
    """
    return x - x.mean()

def calcular_puntos(monto):
    """
    Calcula puntos de lealtad basados en escalones de gasto.
    
    Por qué: Para incentivar el aumento del gasto promedio mediante 
    una iiciativa de recompensas escalonada.
    
    Args:
        monto (float): El valor total de la transacción.
        
    Returns:
        float: Cantidad de puntos asignados.
    """
    if monto > 1000:
        return monto * 0.15  # 15% del total en puntos
    elif monto > 750:
        return monto * 0.1   # 10% del total en puntos
    elif monto > 150:
        return monto * 0.05  # 5% del total en puntos
    else:
        return 0             # Sin puntos para compras bajas