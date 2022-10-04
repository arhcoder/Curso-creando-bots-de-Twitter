import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#! IMPORTANTE LEER https://developer.spotify.com/documentation/web-api/ #

# Para rolas de Led Zeppelin #
#? Para obtener el URI de un artista...
#? IR AL PERFIL DEL ARTISTA, COPIAR EL URL Y SEPARAR...
#/ https://open.spotify.com/artist/     36QJpDe2go2KgaRleHCDTp
#* URI = "spotify:artist:<colocar lo separado en el link>" #
uriLedZeppelin = "spotify:artist:36QJpDe2go2KgaRleHCDTp"


# Credenciales #
# TODO: --------------------------------------------------
#! ESCONDER ESTAS CREDENCIALES EN UN ARCHIVO NO LEGIBLE #
CLIENT_ID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
CLIENT_SECRET = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

#? Crea la conexión a la API y trae los resultados de una petición #
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))
results = spotify.artist_top_tracks(uriLedZeppelin)

#* Estructura para guardar info del top de Led Zeppelin #
names = []
tracks = []
covers = []

print()
#/ Lee los tracks y guarda los datos #
for track in results["tracks"][:10]:

    print("Canción : " + track["name"])
    print("Audio   : " + track["preview_url"])
    print("Portada : " + track["album"]["images"][0]["url"])
    print()

    # names.append(track["name"])
    # tracks.append(tracks["preview_url"])
    # covers.append(track["album"]["images"][0]["url"])

# Imprime los álbums #

'''' for song in range(0, 10):

    print("Canción : " + names[song])
    print("Audio   : " + tracks[song])
    print("Portada : " + covers[song])
    print()
'''