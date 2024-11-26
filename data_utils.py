import csv
import json

def save_data(data):
    # Guardar en CSV
    with open("producto_info.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Producto", "Precio"])  # Encabezados
        writer.writerow([data["Producto"], data["Precio"]])  # Datos

    # Guardar en JSON
    with open("producto_info.json", "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)
