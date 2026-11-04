# Arnesh
# project.py

import random
# pip install pandas
import pandas as pd
import ast


def load_dataset(dataframe):
    """ Load dataset """
    # load the csv file
    df = pd.read_csv(dataframe)
    # return it into the program
    return df


def filter_content(dataframe, genres, release_date, content_type):
    """Clean and filter the columns with from the dataframe"""
    # Drop/remove columns that are not needed
    clean = dataframe.drop(columns=["id", "description",
                                    "age_certification", "runtime", "seasons", "imdb_id", "imdb_score",
                                    "imdb_votes", "tmdb_popularity", "tmdb_score", "production_countries"])
    # Filter the columns by the genre chosen by the user
    genre_filtered = clean[clean['genres'].str.contains(genres, case=False, na=False)]
    # Filter the columns by the release_date chosen by the user
    release_date_filtered = genre_filtered[genre_filtered['release_year'] == release_date]
    # Filter the columns by the content_type chosen by the user
    content_type_filtered = release_date_filtered[release_date_filtered['type'] == content_type]
    # print(content_type_filtered)
    filtered_content = content_type_filtered
    # return filtered content
    return filtered_content


def recommend_content(filtered_content):
    # return 5 random movies or shows
    try:
        return filtered_content.sample(5)
    # if there are less than 5 rows of content it will raise a ValueError
    # this will warn the user and return all available matches
    except ValueError:
        print()
        print("WARNING!! Less than 5 results found. Showing all available matches")
        return filtered_content


def get_unique_genres(dataframe):
    """Return a sorted list of unique genres from the dataset"""
    # in the genre column, drop null/empty values
    # ast library converts a list in a string into a actual list
    # rather than using a FOR loop, apply converts all rows into a list
    genres = dataframe["genres"].dropna().apply(ast.literal_eval)
    # splits elements in the list in seperate rows
    genres = genres.explode()
    # drops null/empty values and removes duplicates
    genres = genres.dropna().unique()
    # return the available genres are sorted in alphabetical order
    return sorted(genres)


def main():
    """ Runs the program """
    # load dataset
    dataframe = load_dataset("titles.csv")
    # ask user for their name
    name = input("Enter your name: ").strip().title()
    # list of genres
    unique_genres = get_unique_genres(dataframe)
    # show user genres
    print(unique_genres)
    # Ask user the genre until it's valid
    while True:
        # ask user for genre
        genre = input("Enter a genre: ").strip().lower()
        # check if user's choice is available or is in the list of genres
        if genre not in unique_genres:
            # reprompt if it's invalid
            continue
        else:
            # end loop if it's valid
            break
    # list of release dates
    list_of_dates = sorted(dataframe['release_year'].unique())
    # print list of release dates
    print(list_of_dates)
    # Ask user the release date until it's valid
    while True:
        try:
            # ask user for release date
            release_date = int(input("Enter a release date: "))
            # check if user's choice is available or is in the list of dates
            if release_date in list_of_dates:
                # end loop if it's valid
                break
        except ValueError:
            # if the input isn't a integer, reprompt the user
            continue
    # list of content type
    list_of_content_type = dataframe['type'].unique()
    # ask user for content_type until it's valid
    while True:
        content_type = input("Enter a content type (MOVIE or SHOW): ").strip().upper()
        # check if user's choice is available or is in the list of content
        if content_type in list_of_content_type:
            # end loop if it's valid
            break
    # filter content to user preference
    filtered_content = filter_content(dataframe, genre, release_date, content_type)
    # create reccomendations for the user
    recommended_content = recommend_content(filtered_content)
    # new line
    print()
    # print the users name and the content type chosen
    print(f"Hello {name}, here are some recommended {content_type.lower()}'s: ")
    # print the recommended content for the user
    print(recommended_content)


# checks if the project file is being run directly, not when it is imported in another python file
if __name__ == "__main__":
    main()
