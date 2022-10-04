from lyricsgenius import Genius

'''
    LEYENDO https://docs.genius.com/#/songs-h2 SE DESCUBRE QUE
    PARA OBTENEY EL LYRICS DE UNA CANCIÓN, PRIMERO HAY QUE SABER
    EL ID DE LA CANCIÓN ... AAAAAAAAAAH!!!
'''

#! http://api.genius.com/search?q={search_term}&access_token={client_access_token} #

genius = Genius("kePhLRukAjzj2ELECp4zAh9Nc-4HzE002017OEXRTK47E8ZfkSszT_n2LVRYMVal")
genius.search_artist('Andy Shauf')
# artist.save_lyrics()