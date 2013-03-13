'''
Created on 13-Mar-2013

@author: rahul
'''
from EngineOperations import EngineOperations
import os

class MoviesEngine:
    def __init__(self):
        self.path = os.getenv("HOME")
        myFile = open(self.path+"/path.conf","r")
        self.path = myFile.readline()
        self.path = self.path[:-1]
        myFile.close()
    def do_analysis(self):
        path = self.path
        x = EngineOperations(path+"/small_movie.data", path+"/small_user.data", path+"/small_ratings.data", path+"/small_genre.data")
        x.top_movie_by_genre()
        x.top_movie_by_year()
        x.top_movie_by_genre_and_year()
        x.most_watched_movie()
        x.most_watched_genre()
        x.highest_rated_genre()
        x.most_active_user()

if __name__=='__main__':
    movie_engine = MoviesEngine()
    movie_engine.do_analysis()