#/ Programa hecho por Charly :3

#* Importa la función de nuestro archivo local que programamos (pokemon.py)...
from pokemon import PokeAPI

#* Importa el campo label para poder ser usado...
from cProfile import label

#* Con esto se hace una ventana, es la interfaz por defecto para crearlas...
import tkinter as tk

#* Importa algunas características y variables...
from tkinter import CENTER, Label, ttk

#? Estas lineas permiten construir una ventana:
ventana = tk.Tk()

#? Le asigna un título:
ventana.title("PokeAPI")  

#? Cambia las dimensiones:
ventana.geometry("580x680")

#? Cambia el color:
ventana['bg']='#E0DEFC'

#? Permite crear una etiqueta de texto para el título:
titulo = Label(ventana, text="\n¡Pokedex!")

#? La posiciona en el centro:
titulo.pack(anchor=CENTER)

#* Cambia algunas de sus configuraciones:
#* por ejemplo el color de la letra, el fondo,
#* la fuente y tamaño:
titulo.config(fg="#9184F7",    # Foreground -> Color de letra;
            bg="#E0DEFC",   # Background -> Color de fondo;
            font=("Verdana",32, "bold")) 

titulo = Label(ventana, text="\nIngresa el nombre del Pokémon")
titulo.pack(anchor=CENTER)
titulo.config(fg="#7BB4F3",  # Foreground -> Color de letra;
            bg="#E0DEFC",   # Background -> Color de fondo;
            font=("Verdana",20)) 

#? Crea un cuadro para entrada de texto:
#? Lo posiciona en las coordenadas marcadas:
barraTexto = ttk.Entry()
barraTexto.place(x=190, y=180)

#/ FUNCIÓN QUE SE EJECUTA CUANDO CLIQUEAS EN "Buscar":
def buscarPokemon():

    #? Guarda en la variable Pokemon lo que haya en
    #? la barra de texto "barraTexto":
    pokemon = barraTexto.get()

    # Lo imprime:
    PokeAPI(pokemon)

#/ EL BOTÓN TIENE LA FUNCIÓN "buscarPokemon":
boton = ttk.Button(text="Buscar", command=buscarPokemon)
boton.place(x=240, y=250)

#/ Abre la ventana:
ventana.mainloop()