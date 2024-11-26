import csv
import json

def save_data(data):
    if not data:
        print("No hay datos para guardar.")
        return
    
    # Guardar en CSV
    with open("producto_info.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Producto", "Precio"])
        writer.writerow([data["Producto"], data["Precio"]])
    print("Datos guardados en producto_info.csv")
    
    # Guardar en JSON
    with open("producto_info.json", mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print("Datos guardados en producto_info.json")
