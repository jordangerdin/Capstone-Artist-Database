from peewee import *
from .config import db_path
from model.Model import Artist
from model.Model import Artwork
from exceptions.artist_error import ArtistError

db = db_path

class SQLArtistDB():

    def insertArtist(self, name, email):

        # Check for empty entries
        if name is None:
            raise ArtistError('Name must not be empty')
        if email is None:
            raise AristError('Email must not be empty')

        # Add to Artist table
        Artist.create(name=name, email=email)

    def insertArtwork(self, artist, artwork, price, available):

        # Add to Artwork table
        Artwork.create(artist=artist, artwork = artwork, price = price, available = available)

    def getAllArtworksByArtist(self, artist_id):
        query = Artwork.select().where(Artwork.artist == artist_id).dicts()
        for row in query:
            print(row['available'])
        return query
    
    def getAllAvailableArtworksByArtist(self, artist_id):
        query = Artwork.select().where(
            (Artwork.artist == artist_id) & 
            (Artwork.available == True)).dicts()
        return query

    def deleteArtwork(self, artwork):
        try:
            work = Artwork.get(Artwork.artwork == artwork)
            work.delete_instance()
        except Exception as err:
            print(str(err))
    
    def getAllArtists(self):
        query = Artist.select().dicts()
        return query
    