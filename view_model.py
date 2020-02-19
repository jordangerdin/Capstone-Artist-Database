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

    def deleteArtwork(self, artwork):
        self.db.deleteArtwork(artwork)

    #def modifyArtwork(self, artist, artwork, price, available):
    #    self.db.modifyArtwork(artist, artwork, price, available)

    def getAllArtists(self):
        return self.db.getAllArtists()
        