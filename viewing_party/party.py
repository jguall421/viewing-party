# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if title is None:
        return None
    if genre is None:
        return None
    if rating is None:
        return None
    
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating

    return movie_dict


def add_to_watched(user_data, movie):

    movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
        }
    
    user_data = {}       
    user_data["watched"] = movie
    print(user_data)
    
    return user_data


user_data = {
        "watched": []
    }
movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
        }

add_to_watched(user_data, movie)

def add_to_watchlist(user_data, movie):
    pass
        
def watch_movie(user_data, title):
    pass




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

