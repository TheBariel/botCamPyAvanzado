import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.meteorologia.gov.py/")
soup = BeautifulSoup(page.content,'html.parser')
vientos = soup.find_all("div",class_="wind col-forecast-today")
temp = soup.find_all("span",class_="temp-max")
ciudades = soup.find_all("span",class_="city")
#print(ciudades)
cont = 0
cont2 = 0
for vaux in vientos:
    vaux = vaux.find_all("span",class_="speed")
    print("\n",ciudades[cont].get_text(),":")
    cont=+2
    print("Temperatura :",temp[cont2].get_text()," C")
    cont2=+1
    print("Vientos :",vaux[0].span.get_text(),"km/h")
