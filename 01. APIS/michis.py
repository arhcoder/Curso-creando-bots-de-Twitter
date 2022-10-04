'''
    RECUERDA HACER ÉNFASIS EN QUE VISUAL STUDIO CODE DA LA DOCUMENTACIÓN
    AL PUNER EL PUNTERO SOBRE "requests", DESDE AHÍ SE PUEDE COMENZAR A
    COMPRENDER QUÉ ES LO QUE HACE LA LIBRERÍA.
'''
import requests

'''
    AL LEER LA DOCUMENTACIÓN SE ENTIENDE QUE LA LIBRERÍA TE PERMITE USAR
    LA FUNCIÓN "get()", Y ESTA REGRESA ALGO QUE DEBE SER GUARDADO EN
    UNA VARIABLE. ADEMÁS, SE PUEDE COLOCAR EL CURSOR SOBRE LA FUNCIÓN
    YA ESCRITA EN EL EDITOR, PARA VER QUÉ SOLICITA DE PARÁMETROS.

    VALE LA PENA ADEMÁS EXPLICAR QUE AL COLOCAR "requests.", EL AUTO-
    COMPLETADOR DE VISUAL STUDIO CODE FILTRA LAS FUNCIONES Y CLASES QUE
    POSEÉ "requests", Y A SU VEZ, AL ESCRIBIRLAS Y COLOCAR EL CURSOR SOBRE
    ESTAS, SE VE SU FUNCIONAMIENTO.

    TAMBIÉN VALE LA PENA RECORDAR QUE AL DAR CLICK DERECHO SOBRE UNA FUNCIÓN
    O LIBRERÍA O CLASE, O LO QUE SEA, SE PUEDE ENCONTRAR LA OPCIÓN "Ver
    definición", QUE TE LANZA HASTA EL CÓDIGO DE LO QUE ESTÁS CLIQUEANDO.

    TAMBIÉN VALE LA PENA RECORDAR QUE, AL ESTAR ESCRIBIENDO Y PRESIONAR
    Ctrl + Espacio, TE SUGIERE QUÉ DEBERÍAS ESCRIBIR, EJEMPLO; DENTRO DE LOS
    PARÉNTESIS DEL MÉTODO, TE DICE QUÉ PARÁMETROS PUEDES COLOCAR.
'''

#! EN OTROS LENGUAJES SE UTILIZA EL TÉRMINO "fetch" PARA
#! REFERIRSE A LA FUNCIÓN QUE CONSUME APIS....
urlDeLaAPI = "https://api.thecatapi.com/v1/images/search"
respuestaDelRequest = requests.get(url=urlDeLaAPI)
print(respuestaDelRequest)

'''
    ESCRIBIR "print(respuestaDelRequest." Y VER CÓMO VSCODE AUTO-
    COMPLETA Y TE DICE QUÉ ATRIBUTOS PUEDES OBTENER DE AHÍ.
'''

'''
    INTENTAR CON EL CÓDIGO SIGUIENTE PARA COMPROBAR LO DE ARRIBA:
    print("Status: " + respuestaDelRequest.status_code + "\n\n")

    DESPUÉS USAR EL SIGUIENTE CÓDIGO...
'''

print(f"Status: {respuestaDelRequest.status_code}\n")
print(f"Content: {respuestaDelRequest.content}\n")
print(f"Text: {respuestaDelRequest.text}\n")
print(f"URL: {respuestaDelRequest.url}\n")
print(f"Headers: {respuestaDelRequest.headers}\n")
print(f"_Content: {respuestaDelRequest._content}\n")
print(f"Encoding: {respuestaDelRequest.encoding}\n")

# Obtener el link de la imagen de gatito #
# Primero se necesita convertir a un JSON #
#* print("\n\n", respuestaDelRequest.json())
respuestaEnJSON = respuestaDelRequest.json()
print(respuestaEnJSON)

'''
    El JSON luce así...
    * Los corchetes indican que es un vector...
    * Cuando se quiere acceder al elemento de un vector, se usan
      corchetes con un número, para indicar cuál elemento...
    [
        * Las llaves indican que es un objeto...
        * Cuando se quiere acceder al valor de un atributo, se
          coloca ["nombreDelAtributo"]...
        {
            "nombreDelAtrbuto": "valorDelAtributo"
        }
    ]
'''

# Queremos obtener el atributo "url", para saber dónde está
# la foto del gato, y este atributo está en el [0]["url"]...
'''
    Elemento [0]...
    [
        Atributo ["url"]...
        {
            "id": "MTcyNTg3OA",
            "url": "https://cdn2.thecatapi.com/images/MTcyNTg3OA.png",
            "width": 160,
            "height": 160
        }
    ]
'''
urlFotoGatito = respuestaEnJSON[0]["url"]
print(urlFotoGatito)

# Se usa una librería para abrir la foto del gatito #
# Esta librería ya está incluída dentro de Python 3 #
import webbrowser
webbrowser.open(urlFotoGatito)