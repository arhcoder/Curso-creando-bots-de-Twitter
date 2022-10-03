<hr>

# 🤖 Creando BOTS de Twitter con Python y Web Scraping

<hr>

#### 📅 Impartido 3, 4 y 5 de Octubre, 2022
#### ⏰ Seis horas teórico-prácticas
#### 💻Congreso de Ciencias Básicas
#### 🏫 Universidad Autónoma de Aguascalientes
#### 🌮 En Español

<hr>

### 📋 Requisitos

#### 🛠 Instalaciones:
- [**Python**](https://www.python.org/downloads/ "Python");
- [**JSON-Handle**](https://chrome.google.com/webstore/detail/json-handle/iahnhfdhidomcpggpaimmmahffihkfnj "JSON-Handle - Chrome");
- [**Visual Studio Code**](http://https://code.visualstudio.com/ "Visual Studio Code");
	* Extensión [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python "Python");
	* Extensión [Better comments](https://marketplace.visualstudio.com/items?itemName=aaron-bond.better-comments "Better comments");
	* Extensión [JSON](https://marketplace.visualstudio.com/items?itemName=ZainChen.json "JSON");

#### 🐦 Cuentas:
- [**Twitter**](https://twitter.com/ "Twitter");
- [**Twitter Developer Portal**](https://developer.twitter.com "Twitter Developer Portal");
- [**Spotify Developer Portal**](https://developer.spotify.com/ "Spotify Developer Portal") (Opcional);
- [**Marvel Developer Portal**](https://developer.marvel.com) (Opcional);

<hr>

## 🗂 Índice
### [1️⃣ Primer día](#1%EF%B8%8F⃣-primer-día-1);
### [2️⃣ Segundo día](#2%EF%B8%8F⃣-segundo-día-1);
### [3️⃣ Tercer día](#3%EF%B8%8F⃣-tercer-día-1);

<hr>

<br>

## 1️⃣ Primer día
### 📚 Tópicos
1. Teoría sobre internet, bots, scraping y APIS.
2. Primer loggeo en la plataforma de desarrollador de Twitter.
3. Definición y partes de un HTTP Request.
4. Ejercicio sobre APIS:
	* Extraer y abrir fotos aleatorias de gatos.
	* Traer datos interesantes sobre Pokémons.
	* Traer canciones más populares de una banda, con Spotify.
	* Ejercicio con API de Marvel.

### 📓 Apuntes

<hr>

#### 🔰 Librería en Python para hacer peticiones http:

Instalación en consola:
```
python -m pip install requests
```
O bien:
```
pip install requests
```

Importación en código:
```
import requests
```

#### 🔰 Ejemplo de uso para hacer petición **GET**:
```python
# Se guarda en "respuesta", el resultado de hacer la petición GET:
respuesta = requests.get("https://api.thecatapi.com/v1/images/search")
print(respuesta) # ---> Imprime algo como <Response[200]>;

# Para obtener los meta-datos que trae la petición:
estatus = respuesta.status_code
cabezera = respuesta.headers
contenido = respuesta.content
texto = respuesta.text
contenidox = respuesta._content
encoding = respuesta.encoding

# Se convierte la respuesta a un archivo JSON para procesarlo:
respuestaEnJSON = respuesta.json()
print(respuestaEnJSON) # ---> Imprime el JSON de la respuesta>;

# SI QUERÉMOS SÓLO EL CONTENIDO DE LA RESPUESTA:
contenidoRespuesta = respuesta.content

# SI EL CONTENIDO DE LA RESPUESTA ES CÓDIGO HTML;
# ES NECESARIO DECODIFICARLO PARA EVITAR ERRORES CON CARACTERES ESPECIALES:
contenidoRespuesta = respuesta.content.decode("utf-8")
```

#### 📖 Para entender cómo leer y procesar JSONs:
- [**Cómo leer JSON**](https://developer.mozilla.org/es/docs/Learn/JavaScript/Objects/JSON "Cómo leer JSON");
- [**Manejo de JSON con Python**](https://pywombat.com/articles/json-python "Manejo de archivos JS con Python");
- [**VIDEO: ¿Cómo abrir los archivos JSON?  Python**](https://www.youtube.com/watch?v=4jnel2Kd9MU "VIDEO: ¿Cómo abrir los archivos JSON? Python");

#### 🧰 Recursos:
- [**LISTA CON CIENTOS DE APIS GRATUITAS PARA USAR**](https://github.com/public-apis/public-apis);
- [**API PARA FOTOS DE GATOS**](https://api.thecatapi.com/v1/images/search);
- [**API PARA FOTOS DE PERROS**](https://random.dog/woof.json);
- [**API PARA FOTOS DE AJOLOTES**](https://axoltlapi.herokuapp.com/);
- [**API PARA FRASES ALEATORIAS**](https://api.quotable.io/random);
- [**API PARA DATOS INTERESANTES INÚTILES**](https://uselessfacts.jsph.pl/);
- [**API DE POKEMÓN**](https://pokeapi.co/);
- [**API DE MARVEL**](https://developer.marvel.com/) (REQUIERE KEYS);
- [**API DE SPOTIFY**](https://developer.spotify.com/) (REQUIERE KEYS);

<hr>

<br>

## 2️⃣ Segundo día
### 📚 Tópicos
1. ¿Qué es el scraping?
2. ¿Qué es xPath?
3. Implementando xPath en el navegador:
	* Extraer frases celebres.
	* Extraer información sobre libros.
4. Ejercicios en Python:
	* Obtener letra de una canción dicha por el usuario.
	* Obtener descuentos en juegos populares de Steam.

### 📓 Apuntes

<hr>

#### 🔰 xPath:
**⭕ Revisar** [**carpeta de apuntes**](https://github.com/arhcoder/Curso-creando-bots-de-Twitter/tree/master/Apuntes/xPath);

#### 🔰 xPath en Python:
Instalar librería
```
python -m pip install lxml
```
O bien:
```
pip install lxml
```

Importación en código:
```
import lxml.html as html
```

**❗ NOTA:** También necesitarémos la librería antes mencionada ***requests***.

#### 🔰 Ejemplo de uso de hacer scraping:
```python
# Hacer request para la página que se desea scrapear:
respuesta = requests.get(urlDeLaWeb)

# Obtener el content del response (Que en este caso
# es un HTML, en lugar de un JSON, como antes). Este
# se debe decodificar con "utf-8" para evitar errores
# en el formato de caractéres especiales:
htmlDeLaWeb = respuesta.content.decode("utf-8")

# Se utiliza la librería que importamos con el nombre
# de "html" para convertir el HTML a un objeto que
# podrá procesar la librería con xPath:
htmlParaScrapear = html.fromstring(htmlDeLaWeb)

# Hacemos scraping a la página y guardamos el resultado:
consultaXPATH = '//a[@class="song"]/text()'
resultadoDelScraping = htmlParaScrapear.xpath(consultaXPATH)
```

#### 🔰 Funciones útiles de Python para procesar texto:
- **Eliminar los espacios de un texto al principio y al final:**
```
nombreCancion = nombreCancion.strip()
```
- **Eliminar los espacios duplicados en un texto:**
```
nombreCancion = " ".join(nombreCancion.split())
```
- **Reemplazar los espacios de un texto por "%20"...**
```
nombreCancion = nombreCancion.replace(" ", "%20")
```

#### 📖 Para entender cómo recorrer listas con Python:
- [**Cómo recorrer listas con *for***](https://es.acervolima.com/iterar-sobre-una-lista-en-python/ "Cómo recorrer listas con for");
- [**Cómo recorrer listas con *for enumerate***](https://www.codigopiton.com/como-recorrer-dos-listas-a-la-vez-en-python/#:~:text=Una%20manera%20sencilla%20de%20recorrer,ambos%20de%20la%20misma%20posici%C3%B3n "Cómo recorrer listas con for enumerate");
- [**VIDEO: Bucle For de string y lista**](https://www.youtube.com/watch?v=dBXs2gRMAJY "VIDEO: Bucle For de string y lista");

#### 🧰 Recursos:
- [**WEB PARA PRACTICAR SCRAPING**](https://toscrape.com/);
	- [**SCRAPING DE FRASES**](http://quotes.toscrape.com/);
	- [**SCRAPING DE LIBROS**](http://books.toscrape.com/);
- [**WEB PARA OBTENER LETRAS DE CANCIONES**](https://lyricsfreak.com/);
- [**WEB ALTERNA DE LETRAS DE CANCIONES**](https://genius.com/);
- [**WEB ALTERNA DE LETRAS DE CANCIONES**](https://metrolyrics.pro/);

<hr>

<br>

## 3️⃣ Tercer día
### 📚 Tópicos
1. Explorar funciones básicas de la API de Tweeter.
2. Ejercicios básicos con Twitter:
	* Twittear.
	* Retwitear.
	* Responder menciones.
	* Enviar DMs.
	* Seguir hastags.
3. Programación del proyecto:
	* Identificar web de Steam.
	* Encontrar xPath para traer datos.
	* Hacer scraping en consola.
	* Colocar resultados en Twits.

### 📓 Apuntes

<hr>

#### 🔰 Crear un entorno virtual en Python:
Comando para crearlo:
```
python -m venv venv
```

**❗ NOTA:** PARA CREAR EL ENTORNO VIRTUAL EN CONSOLA NO OLVIDES
CAMBIAR DE DIRECTORIO A DONDE VA A ESTAR EL PROYECTO. Para moverte
de directorio en consola, ejecuta el comando `cd nombredelacarpeta`.

**✔ En Windows:**

Para activarlo:
```
.\venv\Scripts\activate
```
Para desactivarlo:
```
.\venv\Scripts\deactivate.bat
```

**✔ En MAC:**

Para activarlo:
```
source venv\Scripts\activate
```
Para desactivarlo:
```
source venv\Scripts\deactivate.bat
```

#### 🔰 Cómo esconder varibables secretas:
**1.** Primero instala la librería ***python-dotenv***:
```
python -m pip install python-dotenv
```
O bien...
```
pip install python-dotenv
```
**2.** Crea dentro de la carpeta de tu proyecto un archivo de nombre ***.env***.

**3.** En ***.env*** vas a colocar las variables que quieres esconder, junto a su valor, y separadas por un signo **"="**, y una en cada línea. Es recomendable como estándar, colocar el nombre de las variables en letras mayúsculas. Además, no escribas espacios. (EJEMPLO):
```
API_KEY=xxxxxxxxxxxxxxxxxxxx
API_SECRET=0000000000000000000000
TOKEN=000000.xxxxxxxx.0000.XXXXXXX.00
```
**4. Dentro del código en el que quieres acceder a las variables:**
```python
# Importa la función de la librería...
from dotenv import load_dotenv
import os

# Cargar las varibales de entorno con la función...
load_dotenv()

# Obten las variables según el nombre que les pusiste...
llaveDeLaAPI = os.getenv("API_KEY")
secretoDeLaAPI = os.getenv("API_SECRET")
tokenDeLaAPI = os.getenv("TOKEN")
```

***❌ NO OLVIDES EXLUÍR EL ARCHIVO .env EN LOS SEGUIMIENTOS DE TU SISTEMA GESTOR DE VERSIONES (.gitignore) SI VAS A COLOCAR EL CÓDIGO EN UN REPOSITORIO***.

<br>

#### 🔰 CÓMO CONECTAR EL BOT EN MODO "API":

<hr>

```python
# Se genera una variable con las llaves de autenticación:
auth = tweepy.OAuthHandler(API_KEY, API_SECRET, ACCES_TOKEN, ACCES_TOKEN_SECRET)

# Se crea la conexión y se crea la instancia del bot:
bot = tweepy.API(auth)
```
**❗ NOTA:** Este es sólo un método de autenticación; existen muchas variantes que puedes encontrar en [**LA DOCUMENTACIÓN OFICIAL DE TWEEPY**](https://docs.tweepy.org/), en donde también encontrarás los cambios y actualizaciones que pueda sufrir en el futuro.

<br>

#### 🔰 FUNCIONES VALIOSAS PARA MANIPULAR EL BOT:

<hr>

**1. Publica un tweet de sólo texto:**
```python
bot.update_status("¡Que viva Python! 🛐")
```

<br>

**2. Recupera en una lista los últimos [10] tweets del usuario @arhcoder:**
```python
tweets = bot.user_timeline(screen_name="arhcoder", count=10)
print(f"{tweets[3]}") # <--- Meta-datos del 4to Tweet;
```

<br>

**3. Meta-datos que se pueden obtener del "Tweet":**
```python
# Toma el último Tweet del usuario "@arhcoder":
tweet = bot.user_timeline(screen_name="arhcoder", count=1)[0]

print("\n\n* ID del Tweet: "+str(tweet.id))
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
print("\n* El bot sigue al autor? "+str(tweet.user.following))
#! Y MUCHÍSIMAS OTRAS MÁS CARACTERÍSTICAS #
```
<br>

**4. Obtiene un Tweet teniendo su ID:**

**❗ NOTA:** Se puede saber el ID de un Tweet desde su URL; y se puede obtener su URL desde la web, o dando "compartir" desde la aplicación móvil.
El ID se extrae tal que así...
- **URL:** https://twitter.com/usuario/status/   **ID**   ?más información...
- **Ejemplo:** https://twitter.com/arhcoder/status/1460652032994512898?t=N8f3sgkb02Tq5Ff_K8P7Ug&s=19
- **El ID es:** 1460652032994512898;

```python
unTweet = bot.get_status(id="1460652032994512898")
print(f"\n\n{unTweet}") #<--- Imprime los meta-datos del Tweet;
```

<br>

**5. Obtiene información de un usario teniendo su @arroba:**
```python
usuario = bot.get_user(screen_name="arhcoder")
print(usuario) # <--- Toda la información del usuario;
```

<br>

**6. Envía un mensaje directo:**
```python
# Es posible tomar el ID del usuario desde el atributo "id", y es necesario convertirlo a String...
# Sin embargo, el objeto usuario también trae un atributo llamado "id_str", que ya da el ID del usuario en String...
idDelUsuario = str(usuario.id)
idDelUsuario = usuario.id_str
mensaje = "Soy un bot acosador..."

bot.send_direct_message(recipient_id=idDelUsuario, text=mensaje)
```

<br>

**7. Publicar Tweet con un archivo multimedia:**

**❗ NOTAS:**
- Para trabajar con archivos multimedia; tanto para publicarlos en Tweets, como mensajes, como foto de perfil, es necesario usar una función que primero, **sube dentro de la API de Twitter,** el archivo en cuestión...
- Ya habiendo subido el archivo multimedia, **se obtiene el ID** de este al subirlo, y este es el que **se adjunta** dentro del envío/publicación que querámos hacer.
- Si se quiere trabajar con un **archivo de internet,** es necesario primero **descargarlo** localmente y después subirlo.
- Para descargar archivos de internet, basta con utilizar ***requests***.

**a) Para descargar un archivo de internet con el link de la imágen:**
```python
# Nombre del archivo que guardaremos localmente:
nombreArchivo = "michi.jpg"

# Se hace el request:
urlDeLaImagen = "https://cdn2.thecatapi.com/images/df1.jpg"
respuesta = requests.get(urlDeLaImagen, stream=True)

# Si se pudo obtener la respuesta:
if respuesta.status_code == 200:
	# Función que escribe la imágen en el archivo local:
    with open(nombreArchivo, "wb") as archivoLocalDeImagen:
        for pedazo in respuesta:
            archivoLocalDeImagen.write(pedazo)
else:
    print("No se pudo descargar la imágen...")
```

**b) Para subir el archivo a Twiter y obtener su ID:**

**❗ NOTAS:**
- **Restricciones:**
	- Imágenes: max **5MB;**
	- GIFs: max **15MB;**
	- Videos: max **512MB;**
- **La función retorna una lista de "Media"** pues se pueden agregar varios archivos. A la hora de procesarla es necesario **agarrar sólo el primer** elemento si querémos sólo una imágen:

```python
# La lista que retorna es de objeto tipo "Media", por lo cuál, si se quiere obtener el ID, se deberá procesar:
listaMedias = bot.media_upload(filename=nombreArchivo)
```

**c) Para publicar el Tweet con la imágen (Sólo un archivo):**
```python
# Publica el tweet agregando el ID de la imágen:
# "media_ids" recibe listas de IDs, por lo que si se quiere sólo una, se coloca sólo la que se extrajo anteriormente, entre corchetes []:
bot.update_status(status="🐈 Un mishi bonito: ", media_ids=[listaMedias.media_id_string])
```

**d) Si quieres, puedes hacer que se borre el archivo al descargarlo:**
```
os.remove(nombreArchivo)
```

<br>

**8. Publicar Tweet con varios archivos multimedia:**
```python
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
```

<br>

#### 📖 Para complementar el día:
- [**Guardar imágenes de internet localmente**](https://www.adamsmith.haus/python/answers/how-to-download-an-image-using-requests-in-python);
- [**Python - Sentencia "with"**](https://www.geeksforgeeks.org/with-statement-in-python/);
- [**Python + Tweepy para usar Twitter**](https://www.youtube.com/watch?v=fqFAOYh_-bs "**Python + Tweepy para usar Twitter**");

#### 🧰 Recursos:
- [**PLATAFORMA DE DESARROLLADORES DE TWITTER**](https://developer.twitter.com/ "**PLATAFORMA DE DESARROLLADORES DE TWITTER**");
- [**ESPACIO PARA DAR DE ALTA UNA APP DE TWITTER SI YA SE TIENE CUENTA**](https://developer.twitter.com/en/portal/ "**ESPACIO PARA DAR DE ALTA UNA APP DE TWITTER SI YA SE TIENE CUENTA**");
- [**DOCUMENTACIÓN DE TWEEPY PARA CONOCER SUS FUNCIONES**](https://docs.tweepy.org/ "**DOCUMENTACIÓN DE TWEEPY PARA CONOCER SUS FUNCIONES**");
- [**DOCUMENTACIÓN DE TWEEPY CON TODAS LAS FUNCIONES DE LA API EXPLICADAS**](https://docs.tweepy.org/en/stable/api.html "**DOCUMENTACIÓN DE TWEEPY CON TODAS LAS FUNCIONES DE LA API EXPLICADAS**");
- [**TIENDA OFICIAL DE STEAM**](https://store.steampowered.com/ "TIENDA OFICIAL DE STEAM");
- [**PÁGINA DE OFERTAS ESPECIALES DE STEAM**](https://store.steampowered.com/specials/ "**PÁGINA DE OFERTAS ESPECIALES DE STEAM**");