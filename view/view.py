from model.Model import Artist
from model.Model import Artwork
from exceptions.artist_error import ArtistError

class View:

    def __init__(self, view_model):
        self.view_model = view_model

    def add_new_artist(self):
        print('Insert new artist into the database')

        while True:
            name = input('Enter new Artist name: ')
            if not name:
                break

            ## TODO validate email ??
            email = input('Enter email for ' + name + ': ')

            try:
                self.view_model.insertArtist(name, email)
            except ArtistError as e:
                print(str(e))

    def add_new_artwork(self):
        print('Insert new artwork into the database')

        while True:
            name = input('Enter artists name: ')
            if not name:
                break
            
            artwork = input('Enter name of artwork: ')
            if not artwork:
                break
            
            ## TODO validate price as float
            price = input('Enter price of artwork: ')

            ## TODO validate as boolean
            availableInput = input('Is this piece for sale? y/n ')
            if availableInput == 'y':
                available = True
            else:
                available = False
            try:
                self.view_model.insertArtwork(name, artwork, price, available)
            except ArtistError as e:
                print(str(e))

    def show_artworks_by_artist(self, artist):
        #artist = input('Enter an artist to search: ')
        print('All artworks by ' + artist + ':')
        allArtworks = self.view_model.getAllArtworksByArtist(artist)

        for artwork in allArtworks:
            print(artwork['artwork'] + ', $' + str(artwork['price']) + ' For sale: ' + str(artwork['available']))

    def show_available_artworks_by_artist(self, artist):
        #artist = input('Enter an artist to search: ')
        print('All available artworks by ' + artist + ':')
        allAvailableArtworks = self.view_model.getAllAvailableArtworksByArtist(artist)

        for artwork in allAvailableArtworks:
            print(artwork['artwork'] + ', $' + str(artwork['price']))

    def show_all_artists(self):
        print('All artists in database: ')
        allArtists = self.view_model.getAllArtists()
        
        for artist in allArtists:
            print('Name: ' + artist['name'] + ' Email: ' + artist['email'])
            