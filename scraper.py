import requests
from bs4 import BeautifulSoup

def scrape_amazon_product():
    url = "https://www.amazon.com/UltraGlass-Protector-privacidad-inastillable-antiesp%C3%ADa/dp/B0D6NQD6V6"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extraer título del producto
            title = soup.find('span', {'id': 'productTitle'})
            title_text = title.text.strip() if title else "Título no encontrado"
            
            # Extraer precio del producto
            price = soup.find('span', {'class': 'a-price-whole'})
            price_text = price.text.strip() if price else "Precio no encontrado"
            
            print(f"Producto: {title_text}")
            print(f"Precio: {price_text}")
            
            return {"Producto": title_text, "Precio": price_text}
        else:
            print(f"No se pudo acceder a la página. Código de estado: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error al realizar el scraping: {e}")
        return None
