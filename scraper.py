import requests
from bs4 import BeautifulSoup

def scrape_amazon_product():
    url = "https://www.amazon.com/-/es/Apple-iPhone-Pro-Max-Plata/dp/B09LPS396Z/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extraer título
        title = soup.find('span', {'id': 'productTitle'})
        title_text = title.text.strip() if title else "Título no encontrado"
        
        # Extraer precio
        price = soup.find('span', {'class': 'a-price-whole'})
        price_text = price.text.strip() if price else "Precio no encontrado"
        
        print(f"Producto: {title_text}")
        print(f"Precio: {price_text}")
        
        return {"Producto": title_text, "Precio": price_text}
    else:
        print("No se pudo acceder a la página.")
        return None
