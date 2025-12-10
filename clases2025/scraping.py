import requests
from bs4 import BeautifulSoup

url = "https://www.friv.com"

respuesta = requests.get(url)

if respuesta.status_code == 200:
    print("Conexión exitosa")
    
    soup = BeautifulSoup(respuesta.text, "html.parser")
    
   
    print("HTML recibido:")
    print(soup.prettify()[:2000])
    
    print("n" + "="*50 + "n")
    

    elementos_con_onclick = soup.find_all(onclick=True)
    print(f"Elementos con onclick encontrados: {len(elementos_con_onclick)}")
    
    for i, elem in enumerate(elementos_con_onclick[:5]): 
        print(f"\nElemento {i+1}:")
        print(f"Tag: {elem.name}")
        print(f"Onclick: {elem['onclick']}")
        print(f"Elemento completo: {elem}")

else:
    print(f"Hubo un error al hacer la petición {respuesta.status_code}")