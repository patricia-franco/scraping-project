import os
import requests

def setup_chromedriver():
    url = "https://chromedriver.storage.googleapis.com/130.0.6723.116/chromedriver_linux64.zip"
    zip_file = "chromedriver_linux64.zip"
    
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(zip_file, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        
        os.system(f"unzip {zip_file} && mv chromedriver /usr/local/bin/")
        print("ChromeDriver configurado correctamente.")
    else:
        print("Error al descargar ChromeDriver.")
