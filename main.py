from setup_chromedriver import setup_chromedriver
from scraper import scrape_amazon_product
from data_utils import save_data
from analyze_data import analyze_data
from selenium import webdriver

if __name__ == "__main__":
    # Configurar ChromeDriver
    setup_chromedriver()

    # Probar Selenium Manager
    print("Prueba con Selenium Manager:")
    try:
        driver = webdriver.Chrome()  # Selenium Manager manejará ChromeDriver automáticamente
        driver.get("https://www.google.com")
        print("Título de la página:", driver.title)
        driver.quit()
    except Exception as e:
        print(f"Error con Selenium Manager: {e}")

    # Realizar el scraping
    product_data = scrape_amazon_product()

    # Guardar los datos
    save_data(product_data)

    # Analizar los datos
    analyze_data()
