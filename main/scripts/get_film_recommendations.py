import pandas as pd

def check_similar_users(user_id_x, user_id_y, ratings):
    """
    Returns True if users with ids (users_id_x, users_id_y) are similar based on ratings dataframe
    Returns False otherwise
    """
    if user_id_x == user_id_y:
        return False

    joint_ratings = pd.merge(
        ratings[ratings["user id"] == user_id_x],
        ratings[ratings["user id"] == user_id_y],
        on="item id",
    )
    if joint_ratings.empty:
        return False

    joint_ratings["rating_diff"] = abs(
        joint_ratings["rating_x"] - joint_ratings["rating_y"]
    )
    if max(joint_ratings["rating_diff"]) <= 1:
        return True
    return False


def get_recommendations(users: pd.dataframe, 
                        movies: pd.dataframe, 
                        ratings: pd.dataframe, 
                        full_name: str, 
                        method: str, 
                        year: int):
    """
    Return the title of the most highly recommended movie for the given user. 
    All methods should return a movie title that has not yet been rated by the given user.
    If there is more than one movie that meets the condition, the function should return the first 
    movie in alphabetical order. 

    users:     information about users with the columns (user id, full name, age, gender, zip code)
    ratings:   information about movie ratings by users with the columns (user id, item id, rating, timestamp)
    movies:    information about movies with the columns (movie id, movie title and release year)
    full name: full name of the user for whom we want to return one recommended movie
               whose release year is equal to year using one of the three implemented methods 
    method:    method for recommending movie ('by_popularity', 'by_rating' or 'by_similar_users') 
    year:      movie release year
    """

if __name__ == "__main__":
    users_df = pd.read_csv('/home/home02/earshar/data_science/main/data/users.csv')