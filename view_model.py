class ViewModel:

    def __init__(self, db):
        self.db = db

    def insertArtist(self, name, email):
        self.db.insertArtist(name, email)

    def insertArtwork(self, artist, artwork, price, available):
        self.db.insertArtwork(artist, artwork, price, available)

    def getAllArtworksByArtist(self, artist):
        return self.db.getAllArtworksByArtist(artist)
    
    def getAllAvailableArtworksByArtist(self, artist):
        return self.db.getAllAvailableArtworksByArtist(artist)

    def getAllArtists(self):
        return self.db.getAllArtists()
        