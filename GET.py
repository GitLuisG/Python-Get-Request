try:
    import requests
except Error:
    print("pip install requests");
    print(Error);
    
#sitio al que realizamos la peticion
url='https://www.google.com.mx/'
#Respuesta del servidor
response = requests.get(url)
#Se Imprime la cantidad del contenido que se regresa del servidor
print(response.status_code)

content=response.content
print(response.content)

#Se abre un archivo o si no existe se crea un archivo con escritura binaria
file = open('google.html','wb')
#Se agrega el contenido al archivo
file.write(content)
#Cerramos el Archivo
file.close()
