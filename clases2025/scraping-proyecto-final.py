import requests
from bs4 import BeautifulSoup

url = 'https://sunrise.maplogs.com/es/santo_domingo_dominican_republic.16773.html#google_vignette'

pedido_obtenido = requests.get(url)
html_obtenido = pedido_obtenido.text

soup = BeautifulSoup(html_obtenido, "html.parser")

titulo = soup.find('h1')
print('='*80)
print(f'----{titulo.text}-----')
print('='*80)
print('1. Enero      |      7. Julio')
print('2. Febrero    |      8. Agosto')
print('3. Marzo      |      9. Septiembre')
print('4. Abril      |      10. Octubre')
print('5. Mayo       |      11. Noviembre')
print('6. Junio      |      12. Diciembre')
print('0. Salir')
while True:
   try:
    Mes = int(input('-----------------Ingresa una opcion: '))
    if Mes < 0 or Mes > 12:
       print('⚠️.  Selecciona un mes valido.')
       continue
    if Mes == 0:
       print('Hasta luego.👋')
       exit(0)
    else:
       break
   except ValueError:
      print('⚠️.  El mes debe ser un numero.')
      


if Mes == 1:
 print('='*40)
 print('---Salida y puesta de sol de Enero---')
 print('='*40)

 for fila in soup.find_all("tr"):
     columnas = fila.find_all("td")

     if len(columnas) < 4:
        continue

     fecha    = columnas[0].get_text(strip=True)
     salida  = columnas[1].get_text(strip=True)
     puesta  = columnas[2].get_text(strip=True)
     duracion = columnas[3].get_text(strip=True)

     if "ene." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')
        


if Mes == 2:
 print('='*40)
 print('---Salida y puesta de sol de Febrero---')
 print('='*40)

 for fila2 in soup.find_all("tr"):
    columnas = fila2.find_all("td")

    if len(columnas) < 4:
        continue

    fecha    = columnas[0].get_text(strip=True)
    salida  = columnas[1].get_text(strip=True)
    puesta  = columnas[2].get_text(strip=True)
    duracion = columnas[3].get_text(strip=True)

    if "feb." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')

    
if Mes == 3:
 print('='*40)
 print('---Salida y puesta de sol de Marzo---')
 print('='*40)

 for fila2 in soup.find_all("tr"):
    columnas = fila2.find_all("td")

    if len(columnas) < 4:
        continue

    fecha    = columnas[0].get_text(strip=True)
    salida  = columnas[1].get_text(strip=True)
    puesta  = columnas[2].get_text(strip=True)
    duracion = columnas[3].get_text(strip=True)

    if "mar." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')
        
if Mes == 4:
 print('='*40)
 print('---Salida y puesta de sol de Abril---')
 print('='*40)

 for fila2 in soup.find_all("tr"):
    columnas = fila2.find_all("td")

    if len(columnas) < 4:
        continue

    fecha    = columnas[0].get_text(strip=True)
    salida  = columnas[1].get_text(strip=True)
    puesta  = columnas[2].get_text(strip=True)
    duracion = columnas[3].get_text(strip=True)

    if "abr." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')



if Mes == 5:
 print('='*40)
 print('---Salida y puesta de sol de Mayo---')
 print('='*40)

 for fila2 in soup.find_all("tr"):
    columnas = fila2.find_all("td")

    if len(columnas) < 4:
        continue

    fecha    = columnas[0].get_text(strip=True)
    salida  = columnas[1].get_text(strip=True)
    puesta  = columnas[2].get_text(strip=True)
    duracion = columnas[3].get_text(strip=True)

    if "may." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')


if Mes == 6:
 print('='*40)
 print('---Salida y puesta de sol de Junio---')
 print('='*40)

 for fila2 in soup.find_all("tr"):
    columnas = fila2.find_all("td")

    if len(columnas) < 4:
        continue

    fecha    = columnas[0].get_text(strip=True)
    salida  = columnas[1].get_text(strip=True)
    puesta  = columnas[2].get_text(strip=True)
    duracion = columnas[3].get_text(strip=True)

    if "jun." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')


if Mes == 7:
 print('='*40)
 print('---Salida y puesta de sol de Julio---')
 print('='*40)

 for fila2 in soup.find_all("tr"):
    columnas = fila2.find_all("td")

    if len(columnas) < 4:
        continue

    fecha    = columnas[0].get_text(strip=True)
    salida  = columnas[1].get_text(strip=True)
    puesta  = columnas[2].get_text(strip=True)
    duracion = columnas[3].get_text(strip=True)

    if "jul." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')

if Mes == 8:
 print('='*40)
 print('---Salida y puesta de sol de Agosto---')
 print('='*40)

 for fila2 in soup.find_all("tr"):
    columnas = fila2.find_all("td")

    if len(columnas) < 4:
        continue

    fecha    = columnas[0].get_text(strip=True)
    salida  = columnas[1].get_text(strip=True)
    puesta  = columnas[2].get_text(strip=True)
    duracion = columnas[3].get_text(strip=True)

    if "ago." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')

if Mes == 9:
 print('='*40)
 print('---Salida y puesta de sol de Septiembre---')
 print('='*40)

 for fila2 in soup.find_all("tr"):
    columnas = fila2.find_all("td")

    if len(columnas) < 4:
        continue

    fecha    = columnas[0].get_text(strip=True)
    salida  = columnas[1].get_text(strip=True)
    puesta  = columnas[2].get_text(strip=True)
    duracion = columnas[3].get_text(strip=True)

    if "sep." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')

if Mes == 10:
 print('='*40)
 print('---Salida y puesta de sol de Octubre---')
 print('='*40)

 for fila2 in soup.find_all("tr"):
    columnas = fila2.find_all("td")

    if len(columnas) < 4:
        continue

    fecha    = columnas[0].get_text(strip=True)
    salida  = columnas[1].get_text(strip=True)
    puesta  = columnas[2].get_text(strip=True)
    duracion = columnas[3].get_text(strip=True)

    if "oct." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')

if Mes == 11:
 print('='*40)
 print('---Salida y puesta de sol de Noviembre---')
 print('='*40)

 for fila2 in soup.find_all("tr"):
    columnas = fila2.find_all("td")

    if len(columnas) < 4:
        continue

    fecha    = columnas[0].get_text(strip=True)
    salida  = columnas[1].get_text(strip=True)
    puesta  = columnas[2].get_text(strip=True)
    duracion = columnas[3].get_text(strip=True)

    if "nov." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')

if Mes == 12:
 print('='*40)
 print('---Salida y puesta de sol de Diciembre---')
 print('='*40)

 for fila2 in soup.find_all("tr"):
    columnas = fila2.find_all("td")

    if len(columnas) < 4:
        continue

    fecha    = columnas[0].get_text(strip=True)
    salida  = columnas[1].get_text(strip=True)
    puesta  = columnas[2].get_text(strip=True)
    duracion = columnas[3].get_text(strip=True)

    if "dic." in fecha:
        print("------------------------------------")
        print(f'Fecha:             {fecha}')
        print(f'Salida de sol:     {salida}')
        print(f'Puesta de sol:     {puesta}')
        print(f'Duracion del dia:  {duracion}')
        print('------------------------------------')