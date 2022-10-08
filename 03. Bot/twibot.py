import tweepy
from dotenv import load_dotenv
import requests
import os

#* Obtenemos las llaves:
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_KEY_SECRET")
ACCES_TOKEN = os.getenv("ACCES_TOKEN")
ACCES_TOKEN_SECRET = os.getenv("ACCES_TOKEN_SECRET")

#* Se generan variables con las llaves de autenticación:
auth = tweepy.OAuthHandler(API_KEY, API_SECRET, ACCES_TOKEN, ACCES_TOKEN_SECRET)

#/ Se crea la conexión y se crea la instancia del bot:
bot = tweepy.API(auth)


#? Publica un Tweet de sólo texto #
# bot.update_status("Un pequeño paso para el hombre, un gran salto para la humanidad 😎")


#? Recupera los últimos [10] tweets del usuario @arhcoder:
#? Aquí "tweets" es una lista, en la que cada elemenro contiene
#? toda la información de cada tweet.
tweets = bot.user_timeline(screen_name="arhcoder", count=10)
#? Imprime la información del 4to tweet de la lista:
print(f"{tweets[3]}")

#? Al recuperar un tweet, se pueden extraer varios datos de este:
tweet = bot.user_timeline(screen_name="arhcoder", count=1)[0]
print("\n\n* ID: "+str(tweet.id))
print("\n* Fecha: "+str(tweet.created_at))
print("\n* Texto: "+str(tweet.text))
print("\n* Dispositivo: "+str(tweet.source))
print("\n* Nombre del autor: "+str(tweet.user.name))
print("\n* Foto de perfil del autor: "+str(tweet.user.profile_image_url))
print("\n* Cantidad de seguidores del autor: "+str(tweet.user.followers_count))
print("\n* Cantidad de seguidos del autor: "+str(tweet.user.friends_count))
print("\n* Fecha de creación de la cuenta del autor: "+str(tweet.user.created_at))
print("\n* Arroba del autor: "+str(tweet.user.screen_name))
print("\n* Descripción del autor: "+str(tweet.user.description))
print("\n* Respondió a un Tweet?: "+str(tweet.in_reply_to_status_id))
print("\n* Respondió a un usuario?: "+str(tweet.in_reply_to_user_id))
print("\n* Respondió a un usuario?: "+str(tweet.in_reply_to_screen_name))
print("\n* Cantidad de me gusta: "+str(tweet.favorite_count))
print("\n* Cantidad de me retweets: "+str(tweet.favorite_count))
print("\n* Sigues al autor? "+str(tweet.user.following))
#! Y MUCHÍSIMAS OTRAS MÁS CARACTERÍSTICAS #


#? Para obtener un Tweet teniendo su ID:
#! NOTA: SE PUEDE OBTENER EL ID DE UN TWEET DESDE SU LINK:
#! CUANDO TÚ QUIERES COMPARTIR UN TWEET, TE DA EL URL DEL
#! TWEET, Y ESTE A SU VEZ CONTIENE EL ID EN:
#! https://twitter.com/nombreDelUsuario/   ID   /más cosas...
unTweet = bot.get_status(id="1460652032994512898")
print(f"\n\n{unTweet}")
#! TENIENDO YA EL TWEET, SE PUEDE OBTENER TODA LA INFORMACIÓN ANTERIOR
#! MENCIONADA Y MUCHA MÁS SOBRE SU AUTOR, Y MUCHO MÁS...


#? Se retwitea un tweet del que le des su ID:
# bot.retweet(id="1460652032994512898")


#? Da "favorito" a un tweet del que le pases su ID:
# otroTweet = bot.get_status(id="1460652032994512898")
# otroTweet.favorite()


#? Obtener la información de un usario:
arhcoder = bot.get_user(screen_name="arhcoder")
print(arhcoder)


#? Enviar mensaje directo a un usuario:
mensaje = "No te asustes, pero estoy funcionando 24/7 estando pendiente de ti 👀"
# bot.send_direct_message(recipient_id=arhcoder.id_str, text=mensaje)


#? Coloca un Tweet con una imágen teniendo la dirección de la imágen.
#? Si se quiere colocar una imágen de internet, se necesita primero descargar...
#? Ya guardada localmente a la altura del script, sólo se usa su nombre de archivo:
urlImagen = "https://cdn2.thecatapi.com/images/df1.jpg"
#! update_status_with_media() ESTÁ DEPRECADO. YA NO SE USA...
# bot.update_status_with_media(status="Un mishi...", filename="Michi.jpg", file=urlImagen)

# Se descarga la imágen:
archivo = "michi.jpg"
respuesta = requests.get(urlImagen, stream=True)
if respuesta.status_code == 200:
    with open(archivo, "wb") as image:
        for parte in respuesta:
            image.write(parte)
else:
    print("No se pudo descargar la imágen...")

# Se necesita primero subir la imágen / video, gif, etc.
# Restricciones:
#   * Image  max 5MB;
#   * GIF    max 15MB;
#   * Video  max 512MB;
# Esta función sube la imágen y retorna el ID al subirla...
#! LA FUNCIÓN RETORNA UNA LISTA, PUES SE PUEDEN AGREGAR VARIOS ARCHIVOS...
#! A LA HORA DE PROCESARLA ES NECESARIO AGARRAR SÓLO EL PRIMER ELEMENTO SI
#! QUERÉMOS SÓLO UNA IMÁGEN...
listaMedias = bot.media_upload(filename=archivo)

# Publica el tweet agregando el ID de la imágen:
bot.update_status(status="Un mishi...", media_ids=[listaMedias.media_id_string])

# Si quieres, puedes hacer que se borre el archivo al descargarlo...
# os.remove(archivo)


#? Publicar un Tweet con varios archivos multimedia:
# Lista con todos los archivos a subir en el Tweet:
archivos = ["michi-01.png", "michi-02.jpg", "michi-03.png", "michi-04.jpg"]

# Lista en donde se van a guardar los IDs de las medias:
mediaIDs = []

# Para cada archivo de la lista de archivos:
for archivo in archivos:

    # Sube a twitter el archivo y obten el "Media":
    mediaDelArchivo = bot.media_upload(archivo)

    # Agrega a la lista de medias el id en string del Media del archivo actual:
    mediaIDs.append(mediaDelArchivo.media_id_string)

# Publica el tweet con los archivos que subiste:
bot.update_status(status="🐱‍👤 Un tweet con demasiados gatos :3", media_ids=mediaIDs)


#! AL COLOCAR "bot." Y PRESIONAR "Ctrl + Espacio" VSCODE NOS DARÁ LA
#! LISTA DE TOOOOOOOOODAS LAS FUNCIONES QUE PODEMOS EJECUTAR. QUE SON
#! MUCHAS, ASÍ COMO SABER QUÉ HACE Y QUÉ REQUIERE CADA UNA...

'''
#* Pide al usuario un @ de Twitter e imprime sus últimos 50 tweets:
usuario = input("\nUsuario de Twitter: @")
tweets = bot.user_timeline(screen_name=usuario, count=50)

for i, tweet in enumerate(tweets):
    print(f"\n\n{i+1}: {tweet.created_at}\n{tweet.text}")
'''