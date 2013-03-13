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
        inmemory = InMemoryDatasets("/home/rahul/small_movie.data", "", "")
        movies = inmemory.create_movie_master()
        
        self.assertEqual(movies['1'].title, 'Toy Story (1995)')

    
if __name__ == '__main__':
    unittest.main()