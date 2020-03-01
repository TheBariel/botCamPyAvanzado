"""Programa realizado para el botcam de python 
en penguin academy por Guillermo Ariel Bobadilla"""

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.hendyla.com/casas.html")
soup = BeautifulSoup(page.content,'html.parser')
#armar el objeto soup con la estructura html de la pagina hendyla
casa = soup.find_all('article',class_='product-item clasificado')
#consultar por el bloque de los productos y almacenar en el diccionario casa
precio = casa[0].find_all('div',class_='detalles-precio clear')
#utilizar el primer valor del diccionario y consultar por el bloque donde se especifica el precio
precio = precio[0].select('p')[0].get_text()
#quitar al precio las ultimas etiquetas html, formatear y convertir a entero
cont = 0
for x in precio:
    cont += 1
    if x == '.':
        inpunto = cont
        break

precio = int(precio[inpunto:].replace(" ",'').replace(".",'')) 

descripcion = casa[0].select('div.desc a')[0].get_text()
#utilizar el primer valor del diccionario y realizar una consultar css para obtener la descripción de la casa

url_publicacion = casa[0].select('div.desc a')[0].get('href')
#usar el diccionario para consultar por css el url de la publicación

url_imagen = casa[0].select('figure.img img')[0].get('src')
#usar el diccionario para consultar por css el url de la imagen

print("------------------------------")
print("Descripción : ",descripcion)
print("Precio : ",precio)
print("Url de la Publicación :\n",url_publicacion)
print("Url de la imagen :\n",url_imagen)
print("-----------------------------")
