import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=vwyZH85NQC4")

#print (toy_story.storyline)
#toy_story.show_trailer()
avatar = media.Movie("Avatar","A marine on an alien planet", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UX182_CR0,0,182,268_AL_.jpg","http://www.youtube.com/watch?v=-9ceBgWV8io")

#print (avatar.storyline)
#avatar.show_trailer()
school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

#print (school_of_rock.storyline)
#school_of_rock.show_trailer()
ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://youtu.be/3YG4h5GbTqU")

#print (ratatoullie.storyline)
#ratatuillie.trailer()
midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
                                 "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                 "http://www.imdb.com/video/imdb/vi853581081?playlistId=tt1605783&ref_=tt_ov_vi")


#print (midnight_in_paris.storyline)
#midnight_in_paris.trailer()
hunger_games = media.Movie("Hunger Games", "A really real reality show",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDg3NzYxMF5BMl5BanBnXkFtZTcwNTgyNzkyNw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "http://www.imdb.com/video/imdb/vi3358368281?playlistId=tt1392170&ref_=tt_ov_vi")
#print (hunger_games.storyline)
#hunger_games.trailer()
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris,
          hunger_games] 
fresh_tomatoes.open_movies_page(movies)
