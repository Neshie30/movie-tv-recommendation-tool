# Arnesh
# test_project.py

import pandas as pd
import pytest
from project import load_dataset, filter_content, recommend_content, get_unique_genres


def test_load_dataset():
    """ Test if the dataset loads as a pandas dataframe and its not empty """
    # load the dataset
    df = load_dataset("titles.csv")
    # check if the function loads the dataset as a pandas dataframe
    assert isinstance(df, pd.DataFrame)
    # checks if the dataframe contains rows
    assert not df.empty


def test_filter_content_check_for_rows():
    """ Test if any rows show when content is filtered """
    # load the dataset
    df = load_dataset("titles.csv")
    # filter dataframe
    filtered = filter_content(df, "action", 2016, "MOVIE")
    # check if the filtered dataframe contains rows
    assert not filtered.empty


def test_filter_content_case_sensitive():
    """ Test if the filtering function returns rows while genre is upper case"""
    # load the dataset
    df = load_dataset("titles.csv")
    # filter dataframe, with the genre capitalized
    result = filter_content(df, "COMEDY", 2020, "MOVIE")
    # check if the filtered dataframe contains one or more rows
    assert len(result) >= 1


def test_recommend_content():
    """ Test that the recommendation function returns at least 5 results """
    # load the dataset
    df = load_dataset("titles.csv")
    # gets recommended content
    result = recommend_content(df)
    # checks if it returns at least 5 recommendations
    assert len(result) >= 5


def test_get_unique_genres():
    """ Test if genres appear in the list of unique genres"""
    # load the dataset
    df = load_dataset("titles.csv")
    # get list of unique genres
    genres = get_unique_genres(df)
    # checks if action is in the list of genres
    assert "action" in genres
    # checks if comedy is in the list of genres
    assert "comedy" in genres
