'''
    #! ------------------------------ !#
    #! ESTE EJERCICIO ESTÁ DESCARTADO !#
    #! ------------------------------ !#
    #! LA PÁGINA DE GENIUS.COM BLOQUÉA #
    #! LA BÚSQUEDA DE LETRAS, POR ENDE #
    #! NO ES BUENA IDEA FORZAR LAS PET #
    #! TICIONES, AUN SI ES POSIBLE.    #
    #! ------------------------------ !#
'''

import requests
import lxml.html as html

def getSongPage():

    '''
        PIDE AL USUARIO UNA CANCIÓN.
        RETONA EL URIL QUE DEBERÍA EJECUTAR
        PARA ENCONTRAR EL LYRICS.
    '''

    # PIDE AL USUARIO EL NOMBRE DE LA CANCIÓN #
    rola = input("\nNombre de una canción: ")

    '''
        EL NOMBRE DE LA CANCIÓN SE DEBERÁ INGRESAR DENTRO
        DE UN URL, POR ENDE, DEBEMOS REEMPLAZAR LOS ESPACIOS
        POR EL EQUIVALENTE A UN ESPACIO DENTRO DE URLS: "%20",
        ADEMÁS DE HACER CIERTAS VALIDACIONES PARA LOS ESPACIOS;
    '''
    # Se eliminan los espacios al principio y al final...
    rola = rola.strip()

    # Se eliminan los espacios duplicados...
    rola = " ".join(rola.split())

    # Se reemplazan los espacios por "%20"...
    rola = rola.replace(" ", "%20")
    # print("\n", rola)

    '''
        YA TENIENDO EL TÍTULO DE LA CANCIÓN, SE PLANTEA QUE
        ESTA SEA REEMPLAZADA EN EL LINK DE BÚSQUEDA EN LA
        PLATAFORMA DE "genius.com", PARA HACER SCRAPING A
        LA LETRA. OBTENIENDO PRIMERO EL HTML...

        https://genius.com/search?q=ROLA
    '''
    geniusSearchURI = "https://genius.com/search?q="

    print(geniusSearchURI + rola)
    return geniusSearchURI + rola


def getSongURL(songURL):

    '''
        HACE LA PETICIÓN A LA WEB DE GENIUS UTILIZANDO LA
        LIBRERÍA REQUESTS PARA OBTENER EL HTML DE LA BÚSQUEDA...
        RETORNA EL HTML...
    '''

    #! EL TRY CATCH DEBE IMPLEMENTARSE DESPUÉS DE LA FUNCIÓN...
    '''
    try:
        songHTMLResponse = requests.get(songURL)

        #* SI LA RESPUESTA FUER CORRECTA #
        if songHTMLResponse.status_code == 200:

            #/ SE GUARDA LA PÁGINA EN UN HTML #
            with open("html-search.html", "w", encoding="utf-8") as file:
                file.write(songHTMLResponse.text)

            #/ AQUÍ SE EXTRAE EL HTML DE LA PÁGINA DE BÚSQUEDA #
            searchPageHTML = songHTMLResponse.content.decode("utf-8")
            # print(searchPageHTML)

            #? AHORA ES NECESARIO UTILIZAR LA EXPRESIÓN DE XPATH
            #? CONSTRUÍDA, PARA OBTENER EL URL DE LA PÁGINA DE LA
            #? CANCIÓN QUE SE BUSCARÁ.
            XPATH_GET_SONG_URL = '/descendant::a[@class="mini_card"][2]/@href'
            HTMLParseado = html.fromstring(searchPageHTML)
            # print(HTMLParseado)
            return HTMLParseado.xpath(XPATH_GET_SONG_URL)

        else:
            raise ValueError("Error ", songHTMLResponse.status_code)
    
    except ValueError as error:
        print(error)
    '''


''' SE EXPLICA QUE ASÍ SE DEFINE UN PUNTO DE EJECUCIÓN '''
if __name__ == '__main__':

    # Punto de ejecución #
    print(getSongURL(getSongPage()))