from view import *

from sql_database.database import SQLArtistDB

from view.view import View
from view_model import ViewModel

def main():
    # Start view, setup high level
    artistDB = SQLArtistDB()

    artistViewModel = ViewModel(artistDB)

    artistView = View(artistViewModel)

    # UI stuff

    artistView.add_new_artist()

    artistView.add_new_artwork()

    artistView.show_artworks_by_artist('Jordan')

    artistView.show_available_artworks_by_artist('Jordan')

    artistView.delete_artwork('Starry Night')

    artistView.show_all_artists()
    

if __name__ == '__main__':
    main()