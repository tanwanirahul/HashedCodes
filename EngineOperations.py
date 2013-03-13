'''
Created on 13-Mar-2013

@author: rahul
'''
from InMemoryDatasets import InMemoryDatasets
import os
class EngineOperations:
    
    
    def __init__(self,movie_file,user_file,rating_file,genres_file):
        in_memory_datasets = InMemoryDatasets(movie_file,user_file,rating_file,genres_file)
        self.movies = in_memory_datasets.movies
        self.users = in_memory_datasets.users
        self.genres = in_memory_datasets.genres
        self.ratings = in_memory_datasets.ratings
        self.genre_movies =in_memory_datasets.genre_movies
        self.year_movies = in_memory_datasets.year_movies
        
    
    def __format(self,title):
            print "\n============================================================="
            print "\t\t\t",title
            print "=============================================================\n"
            
    
    def top_movie_by_genre(self):
        self.__format("Top Movie By Genre")
        for i in self.genres.keys():
            if i in self.genre_movies.keys():
                top = self.__get_top_movie(self.genre_movies[i])
                print "%-20s| %s" % (self.genres[i],self.movies[top].title)
            else:
                print "%20s| No Movie Found For This Genre." % (self.genres[i])
    
    def top_movie_by_year(self):
        self.__format("Top Movie By Year")
        for i in self.year_movies.keys():
            top = self.__get_top_movie(self.year_movies[i])
            print "%-20s| %s" % (i,self.movies[top].title)
    
    def top_movie_by_genre_and_year(self):
        self.__format("Top Movie By Year")
        for i in self.year_movies.keys():
            for j in self.genre_movies.keys():
                common_movies = self.year_movies[i] & self.genre_movies[j]
                if len (common_movies) > 0:
                    top = self.__get_top_movie(common_movies)
                    print "%-20s| %-20s| %s" % (i,self.genres[j],self.movies[top].title)
                else:
                    print "%-20s| %-20s| No Movie Found" % (i,self.genres[j]) 
            print 
            
    def most_watched_movie(self):
        self.__format("Most Watched Movie")
        top = self.__get_most_watched_movie()
        print "%s" % (self.movies[top])
    
    def most_watched_genre(self):
        self.__format("Most Watched Genre")
        top = self.__get_most_watched_genre()
        print "%s" % (self.genres[top])
    
    def highest_rated_genre(self):
        self.__format("Highest Rated Genre")
        top = self.__get_highest_rated_genre()
        print "%s" % (self.genres[top])
    
    def most_active_user(self):
        self.__format("Most Active User")
        top = self.__get_most_active_user()
        print "%s" % (self.users[top])
        
    def __get_top_movie(self,movie_set):
        maxValue = 0;
        movie_id = 0;
        for i in movie_set:
            rate = self.movies[i].total_rates
            if  rate > maxValue:
                movie_id = i
                maxValue = rate
        return movie_id
    
    def __get_most_watched_movie(self):
        maxValue = 0;
        movie_id = 0;
        for i in self.movies.keys():
            rate = self.movies[i].rates_count
            if  rate > maxValue:
                movie_id = i
                maxValue = rate
        return movie_id
    
    def __get_most_watched_genre(self):
        maxValue = 0;
        genre_id = 0;
        for i in self.genre_movies.keys():
            total_count = 0
            for j in self.genre_movies[i]:
                total_count += self.movies[j].rates_count
            if total_count > maxValue:
                maxValue = total_count
                genre_id = i
        return genre_id
    
    def __get_highest_rated_genre(self):
        maxValue = 0;
        genre_id = 0;
        for i in self.genre_movies.keys():
            total_count = 0
            for j in self.genre_movies[i]:
                total_count += self.movies[j].total_rates
            if total_count > maxValue:
                maxValue = total_count
                genre_id = i
        return genre_id
    
    def __get_most_active_user(self):
        maxValue = 0;
        user_id = 0;
        for i in self.users.keys():
            rate = len(self.users[i].movies_set)
            if  rate > maxValue:
                user_id = i
                maxValue = rate
        return user_id
