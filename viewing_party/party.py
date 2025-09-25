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
    watched = user_data["watched"] 
    if watched is None:        
        watched = [movie]
    watched.append(movie)

    return user_data


def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    if watchlist is None:
        watchlist= [movie]
    watchlist.append(movie)

    return user_data

        
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data  

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    average = 0.0
    total = len(user_data["watched"])

    for movies in user_data["watched"]:
        for key, value in movies.items():
            if key == "rating":
                sum += value
            average = sum /total
    return average
                        

def get_most_watched_genre(user_data):
    # create frequency dict
    frequency = {}

    if not user_data["watched"]:
        return None
    
    for movies in user_data["watched"]:
        if not movies["genre"] in frequency:
            frequency[movies["genre"]] = 1
        else:
            frequency[movies["genre"]] += 1

    # compage value and return genre
    most_genre = None
    most_value = 0

    for genre, value in frequency.items():
        if value > most_value:
            most_genre = genre
            most_value = value

    return most_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):

    friends_watched = []
    unique_watched = []


    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie["title"])
    print("friends_watched:", friends_watched)
    friends_watched_set = set(friends_watched)
    


    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched_set:
            unique_watched.append(movie)
    print("user watched", movie)
        
    return unique_watched

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    duplicate_titles = []
    user_watched_titles = []

    for movie in user_data["watched"]:
        if movie["title"] not in user_watched_titles:
            user_watched_titles.append(movie["title"])


    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched_titles:
                if movie["title"] not in duplicate_titles:
                    friends_unique_movies.append(movie)
                    duplicate_titles.append(movie["title"]) 
                
    return friends_unique_movies


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended = []

    friends_unique_movies = get_friends_unique_watched(user_data)
    print("friends_unique_movies:", friends_unique_movies)

    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended.append(movie)

    return recommended

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    pass

def get_rec_from_favorites(user_data):
    pass