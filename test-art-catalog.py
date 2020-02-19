import sqlite3
import unittest
from unittest import TestCase

from sql_database import database
from model.Model import Artist
from model.Model import Artwork
from exceptions.artist_error import ArtistError

MODELS = [Artist, Artwork]

class TestArtistDB(TestCase):

    test_db = 'test_artworks.db'

    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)
    
    def tearDown(self):
        test_db.drop_tables(MODELS)

        test_db.close()

    def test_insert_artist(self):
        artist = Artist('Jordan', 'test@test.com')
        self.db.insertArtist(artist)
        expected = {'Jordan' : 'test@test.com'}
        self.compare_db_to_expected(expected)

    def compare_db_to_expected(self, expected):
        test_db.connect()
        all_data = test_db.select()