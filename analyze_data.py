import pandas as pd

def analyze_data():
    try:
        df = pd.read_csv("producto_info.csv")
        print("Datos cargados:")
        print(df.head())
    except FileNotFoundError:
        print("El archivo CSV no se encontró.")
