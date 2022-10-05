'''
    PRIMERO ES NECESARIO CONOCER LA ESTRUCTURA DEL SITIO WEB
    Y VISUALIZAR EL MODO EN EL QUE ACCEDERÍAMOS A AQUELLO A
    LO QUE QUEREMOS ACCEDER (LETRA DE CANCIÓN), DE MODO MANUAL,
    Y DESPUÉS AUTOMATIZARLO EN ESTE SCRIPT POR EL PROCESO...

    EJEMPLO:

    PARA OBTENER LA LETRA DE UNA CANCIÓN EN lyricsfreak.com:

    1. Se ingresa al sitio web.
    2. Se va a la barra de búsqueda y se coloca el nombre de
       la canción que se quiere buscar.
    3. Se presiona enter para iniciar la búsqueda.
    4. Se busca la primera opción preferiblemente.
    5. Al clicar sobre esta opción, se obtuvo ya la letra
       de la canción que se quería.
    6. Ya se obtuvo la letra de la canción.

    NOTE: NÓTESE QUE LAS ACCIONES FÍSICAS HECHAS DESDE EL
    NAVEGADOR TIENEN UN SEGUIMIENTO LÓGICO; POR EJEMPLO,
    PRESIONAR ENTER EN LA BARRA DE BÚSQUEDA PROVOCA QUE LA
    BARRA DE NAVEGACIÓN DEL NAVEGADOR CAMBIE A UN URL CON
    LOS DATOS QUE BUSCAMOS. TAMBIÉN; CUANDO CLIQUEAMOS SOBRE
    LA CANCIÓN, LO QUE HACEMOS ES ACCEDER AL LINK QUE CONTIENE
    EL ATRIBUTO DE DICHA ETIQUETA.
'''
lyricsfreak = "https://lyricsfreak.com"

'''
#! NOTA IMPORTANTE #
EL CÓDIGO SIGUIENTE ESTÁ ESCRITO SECUENCIALMENTE, AUNQUE COMO
BUENA PRÁCTICA ES MEJOR FRAGMENTARLO EN FUNCIONES. SIN EMBARGO
SE HARÁ DE MANERA SECUENCIAL PARA FACILITAR EL ENTENDIMIENTO DEL
FLUJO DE ACCIONES PARA CONCRETAR EL SCRAPING.
'''


#* 1. Hay que solicitar al usuario el nombre de la canción que desea buscar:
nombreCancion = input("\nCanción a buscar: ")

'''
    Identificamos que para hacer la búsqueda, la web de lyricsfreak.com
    utiliza un link especial de este formato:
        https://lyricsfreak.com/search.php?q=NOMBREDECANCION...
    
    Además; al colocar el nombre de la canción al costado, reemplaza ciertos
    caractéres especiales, como el "espacio", que al no poder escribirse dentro
    de un link, se reemplaza por la cadena %20.
'''

#? Se eliminan los espacios al principio y al final...
nombreCancion = nombreCancion.strip()

#? Se eliminan los espacios duplicados...
nombreCancion = " ".join(nombreCancion.split())

#? Se reemplazan los espacios por "%20"...
nombreCancion = nombreCancion.replace(" ", "%20")

urlBuscarCancion = lyricsfreak+"/search.php?q="+nombreCancion

#* 2. Hay que "entrar" en la página que ya definimos:
#? En la práctica eso se traduce en hacer una petición
#? y obtener el resultado; que no será un archivo JSON,
#? sino un archivo HTML; el cuál debemos obtener...
import requests
import lxml.html as html

try:
    respuesta = requests.get(urlBuscarCancion)

    #? Si el status code de la respuesta es 200, la conexión fue correcta:
    if respuesta.status_code == 200:

        #? "respuesta" tiene guardado un response con los resultados de la
        #? petición, tal como hacíamos con las APIS, extraerémos el text,
        #? que en este caso, un HTML...
        # NOTE: AL SER HTML UN FORMATO COMPLETO, ES RECOMENDABLE PASARLE
        # LA FUNCIÓN "decode("utf-8")", para regularizar el uso de
        # caracéres especiales para la implementación en Python.
        # print(respuesta.content.decode("utf-8"))
        cancionesEncontradasHTML = respuesta.content.decode("utf-8")

        #/ Es necesario convertir el HTML a un formato especial que usa
        #/ la misma librería con la que se hará una búsqueda de xPath...
        cancionesEncontradasHTML = html.fromstring(cancionesEncontradasHTML)

        #* Ejecutamos una consulta de xPath, para obtener los resultados
        #* de la búsqueda en la página, y obtener el link al que llevan...
        #* Una consulta obtiene el artista y otro el nombre de la canción...
        #* Se traen todos los que la página ofrece al hacer la búsqueda...
        XPATH_RESULTADOS_ARTISTAS = '//div[@class="lf-list__row js-sort-table-content-item"]/@data-sorting-artist'
        XPATH_RESULTADOS_CANCIONES = '//a[@class="song"]/text()'
        XPATH_RESULTADOS_LINKS = '//a[@class="song"]/@href'

        #? Se ejecutan las expresiones de xPath para obtener los resultados...
        artistas = cancionesEncontradasHTML.xpath(XPATH_RESULTADOS_ARTISTAS)
        canciones = cancionesEncontradasHTML.xpath(XPATH_RESULTADOS_CANCIONES)
        links = cancionesEncontradasHTML.xpath(XPATH_RESULTADOS_LINKS)

        # print(artistas)
        # print(canciones)
        # print(links)

        #/ Al traer información de la web, vale la pena limpiar los formatos,
        #/ a menudo suelen traer exceso de espacios al inicio y final, o saltos
        #/ de línea innecesarios. Esto es necesario para los elementos de "canciones"
        for i, cancion in enumerate(canciones):
            #? Se eliminan los espacios al principio y al final...
            cancion = cancion.strip()

            #? Se eliminan los espacios duplicados...
            cancion = " ".join(cancion.split())

            #? Se reemplazan los saltos de línea por ""...
            cancion = cancion.replace("\n", "")
            canciones[i] = cancion
        
        # print(canciones)

        #* Si sí se encontró por lo menos un resultado:
        if len(artistas) > 0:

            #/ Se imprimen los resultados de la búsqueda y se le pregunta al usuario qué
            #/ canción quiere elegir; mediante un número:
            print("\n¿Cuál canción buscas?\n")
            for i in range(0, len(artistas)):
                print("[{:}]\t{:<40} {:<40}".format(i+1, canciones[i], artistas[i]))
            numero = int(input("\nNúmero: ")) - 1

            #! AHORA HACE SCRAPING ENTRANDO EN EL LINK CORRESPONDIENTE A LA ELECCIÓN #
            #? Si el usuario colocó un número o dato incorrecto, irá al catch y mostrará el error.
            #* 3. Se "da click" en la canción elegida y se abre y busca la letra #

            # Se hace otra petición al link original + la dirección de la canción...
            respuesta = requests.get(lyricsfreak+links[numero])
            if respuesta.status_code == 200:
                HTMLcancion = respuesta.content.decode("utf-8")
                HTMLcancion = html.fromstring(HTMLcancion)

                XPATH_LETRA = '//div[@id="content"]/text()'
                letra = HTMLcancion.xpath(XPATH_LETRA)

                print("\n\n"+100*"_"+"\n")
                print(f"{canciones[numero].upper()}\n{artistas[numero]}")
                print(""+100*"_"+"\n\n")
                for linea in letra:
                    linea = linea.strip()
                    linea = " ".join(linea.split())
                    linea = linea.replace(" )", ")")
                    print(linea)
                print("\n"+100*"_"+"\n")
        else:
            print("\nNo se encontraron resultados :(\n")
    else:
        raise ValueError("Error ", respuesta.status_code)
    
except ValueError as error:
    print(error)