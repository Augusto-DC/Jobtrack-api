import requests
import json

# Hacemos un pedido GET a la PokéAPI, pidiendo info de Pikachu
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

# Código de estado: 200 significa "todo salió bien"
print("Código de estado:", respuesta.status_code)

# Convertimos la respuesta (que viene en JSON) a un diccionario de Python
datos = respuesta.json()

# Ahora podemos navegar el diccionario como cualquier dict de Python
#print(datos["types"]) Estructura de un diccionario 
#print("Nombre:", datos["name"])
#print("Peso:", datos["weight"])
#print("Tipos:", [tipo["type"]["name"] for tipo in datos["types"]])
#------------------------------

# Guardamos la respuesta completa en un archivo, bien formateada
with open("pikachu.json", "w") as archivo:
    json.dump(datos, archivo, indent=2)

print("Datos guardados en pikachu.json")

# Extraemos y organizamos solo lo que nos interesa
resumen = {
    "nombre": datos["name"],
    "peso": datos["weight"],
    "tipos": [tipo["type"]["name"] for tipo in datos["types"]]
}

print("Resumen:", resumen)

# Guardamos también esta versión resumida
with open("pikachu_resumen.json", "w") as archivo:
    json.dump(resumen, archivo, indent=2)