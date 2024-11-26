import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_python():
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extraer el título de la página
            title = soup.find('h1', {'id': 'firstHeading'})
            title_text = title.text.strip() if title else "Título no encontrado"
            
            # Extraer el primer párrafo
            first_paragraph = soup.find('p')
            paragraph_text = first_paragraph.text.strip() if first_paragraph else "Párrafo no encontrado"
            
            print(f"Título: {title_text}")
            print(f"Primer párrafo: {paragraph_text}")
            
            return {"Título": title_text, "Primer párrafo": paragraph_text}
        else:
            print(f"No se pudo acceder a la página. Código de estado: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error al realizar el scraping: {e}")
        return None
