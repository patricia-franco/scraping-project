from scraper import scrape_amazon_product
from data_utils import save_data
from analyze_data import analyze_data

if __name__ == "__main__":
    # Realizar el scraping de Amazon
    print("Ejecutando scraping de Amazon...")
    product_data = scrape_amazon_product()

    if product_data:
        # Guardar los datos
        print("\nGuardando los datos...")
        save_data(product_data)

        # Analizar los datos
        print("\nAnalizando los datos...")
        analyze_data()
    else:
        print("No se obtuvieron datos del scraping.")
