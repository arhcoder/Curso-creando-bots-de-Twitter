from tkinter import messagebox
import requests
import webbrowser

#  ste es el archivo de la API de Pokémon

#se inicia con una función que hará todo el trabajo
#creada por nostros con el objetivo de pasar esto
#al archivo de la GUI
def PokeAPI(pokemon):

    #envía una solicitud GET al URL especificado
    pokemonResponse = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemon.lower())

    #en base a los códigos de estatus, se hace un IF, si resulta correcto
    #hace lo que se le indica
    if pokemonResponse.status_code == 200:
        pokemonResponse_JSON= pokemonResponse.json()
        especie = pokemonResponse_JSON["species"]["name"]
        altura = pokemonResponse_JSON["height"]
        peso = pokemonResponse_JSON["weight"]
        sprite = pokemonResponse_JSON["sprites"]["other"]["dream_world"]["front_default"]
        webbrowser.open(sprite)
        messagebox.showinfo(message= "Nombre: " + especie + "\n\n Altura: " + str(altura) + "\n\nPeso: " + str(peso) + "\n\nSprite: " + sprite)
        #messagebox.showinfo(message= "Nombre: " + especie + "\n Altura: " + altura + "\nPeso: " + weight)
        #print("Nombre: ", especie, "\n")
        #print("Altura: ", height," \n ")
        #print("Peso: ", weight, " \n ")
        print(sprite)