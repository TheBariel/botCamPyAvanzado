#codigo que utiliza el metodo post en una página
#fuente de la pagina https://github.com/WilliBobadilla/penguin-python-advanced


import requests

datos = {
    'nombre' : "Guillermo",
    'apellido' : "Bobadilla"
}
respuesta = requests.post("https://willidatos.herokuapp.com/form-example",datos)
print(respuesta)
print(respuesta.text)
