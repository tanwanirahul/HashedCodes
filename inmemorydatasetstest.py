'''
Created on 12-Mar-2013

@author: rahul
'''
import unittest
from InMemoryDatasets import InMemoryDatasets

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_movie_master(self):
        inmemory = InMemoryDatasets("/home/rahul/Datasets/small_movie.data", "/home/rahul/Datasets/small_user.data", "/home/rahul/Datasets/small_ratings.data","/home/rahul/Datasets/small_genre.data")
       # movies = inmemory.create_movie_master()
        
        self.assertEqual(inmemory.movies['1'].title, 'Toy Story (1995)')
        self.assertEqual(inmemory.movies['6'].total_rates, 2)
        self.assertEqual(inmemory.movies['7'].rates_count, 3)
        
    