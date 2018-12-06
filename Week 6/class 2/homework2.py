#def make_album(artist_name, album_name, songs=''):
 #   album = {'artist': artist_name, 'album': album_name}
  #  if songs:
   #     album['songs'] = songs
    #return album

#music_catalogue1 = make_album('jimmy page', 'led zep1', songs=13)
#music_catalogue2 = make_album('jimmy hendrix', 'live at wood stock', songs=24)
#music_catalogue3 = make_album('bob dylan', 'knocking at your door', songs=5)
#print(music_catalogue1)
#print(music_catalogue2)
#print(music_catalogue3)


#----------------------------------------------------------------------------------


def get_make_album(artist_name, album_name, ):
    album = artist_name + ' ' + album_name
    return album.title()

while True:
    print("\nplease tell me your favorite album:")
    ar_name = input("artist name:")
    al_name = input("album title:")

    make_album = get_make_album(ar_name, al_name)
    print("\nyour album is, " + make_album + "!")

#------------------------------------------------------------------------





