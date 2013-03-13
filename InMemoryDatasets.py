'''
Created on 12-Mar-2013

@author: rahul
'''
from DataSetsSchema import *

class InMemoryDatasets:
    
    path = ""
        
    def __init__(self, movie_file, user_file, ratings_file, genres_file):
        self.genre_movies = {}
        self.year_movies = {}
        self.movies = self.create_movie_master(movie_file)
        self.users = self.createUsersMaster(user_file)
        self.ratings = self.createRatingsMaster(ratings_file)
        self.genres = self.create_genre_master(genres_file)
#        keys = self.movies.keys()
#        for key in keys:
#            print (key, self.movies[key].title)
            
    def create_movie_master(self,movie_file):
        moviesMaster = {}
        myFile = open(movie_file)
        for line in myFile.readlines():
            line = line [:-1]
            data = line.split("|")
            #print data
            genres=[]
            for i in range (5,len(data)):
                if data[i] == '1':
                    genres.append(str(i-5))
            temp = Movie(data[0],data[1],data[2],data[3],data[4],0,0,genres)
            moviesMaster[data[0]] = temp
        return moviesMaster

    def createUsersMaster(self,user_file):
        usersMaster = {}
        myFile = open(user_file)
        for line in myFile.readlines():
            line = line [:-1]
            data = line.split("|")
            temp = User(data[0],data[1],data[2],data[3],data[4],set())
            usersMaster[data[0]] = temp
        return usersMaster

        
    def createRatingsMaster(self,ratings_file):
        ratingsMaster = []
        myFile = open(ratings_file)
        for line in myFile.readlines():
            line = line [:-1]
            data = line.split()
            #print data
            temp = Rating(data[0],data[1],data[2],data[3])
            ratingsMaster.append(temp)
                
                # Add this movie in the appropriate users's movie set. 

            if data[0] in self.users:
                self.users[data[0]].movies_set.add(data[1])
            
                # Increase the total_rates and rate_count for this movie. 

            if data[1] in self.movies:
                self.movies[data[1]].total_rates+= int(data[2])
                self.movies[data[1]].rates_count+=1
                # Add all the genres of this movies in genre_movies dictionary. 
                #print self.movies[data[1]].genres
                for i in self.movies[data[1]].genres:
                  
                    if i in self.genre_movies.keys():
                        self.genre_movies[i].add(data[1])
                    else:
                        self.genre_movies[i] = {data[1]}

                # Add this movie in the movies set for appropriate year.
            #print self.movies[data[1]].release_date
            year = self.movies[data[1]].release_date.split("-")
            if len (year) == 3:
                year = year[2]
                if year in self.year_movies.keys():
                    self.year_movies[year].add(data[1])
                else:
                    self.year_movies[year] = {data[1]}              
        return ratingsMaster
    
    def create_genre_master(self, genres_file):
        genresMaster = {}
        myFile = open(genres_file)
        for line in myFile.readlines():
            line = line [:-1]
            data = line.split("|")
            genresMaster[data[1]] = data[0]
        return genresMaster
    