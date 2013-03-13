'''
Created on 12-Mar-2013

@author: rahul
'''

class Movie:

    def __init__(self, movie_id, title, release_date, video_release_date, IMDBURL,total_rates,rates_count,genres):
        self.movie_id = movie_id
        self.title = title
        self.release_date = release_date
        self.video_release_date = video_release_date
        self.IMDBURL = IMDBURL
        self.total_rates = total_rates
        self.rates_count = rates_count
        self.genres = genres
    
    def __str__(self):
        return self.title+ ' '+ self.release_date +' '+self.IMDBURL 
     
class User:
    def __init__(self, user_id, age, gender, occupation, zipcode,movies_set):
        self.user_id = user_id
        self.gender = gender
        self.age = age
        self.occupation = occupation
        self.zipcode = zipcode
        self.movies_set = movies_set
    
    def __str__(self):
        return self.user_id+ ' '+ self.gender +' '+self.age+' '+self.occupation + "\nMovies Rated := " + str(len(self.movies_set))

class Rating:
    def __init__(self,user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp
