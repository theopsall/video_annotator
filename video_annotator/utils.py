"""
Helper functions
"""
import os
import pandas as pd
import random
from video_annotator.config import VIDEOS, ANNOTATED, USERS


def get_users() -> list:
    """
    Get Users from user file

    Returns:
        list: List of registered users
    """
    with open(USERS, 'r') as f:
        users = [line.split('\n')[0] for line in f.readlines()]

    return users


def add_user(user) -> None:
    """
    Insert user to the database

    Args:
        user (str): Name of the user to be added
    """
    with open(USERS, 'a') as f:
        f.write(user + '\n')


def add_video(user, video_name) -> None:
    """
    Add video to the user annotated log file

    Args:
        user (str): Name of the current user annotator
        video_name (str): Name of the video that have been annotated
    """
    with open(USERS, 'a') as f:
        f.write(video_name + '\n')


def make_annotation_file(user) -> None:
    """
    Make annotation file containing the annotated videos name by the current user

    Args:
        user (str): Name of the current user annotator
    """
    user_path = os.path.join(ANNOTATED, user)
    with open(user_path + '.txt', 'w') as f:
        pass


def make_annotation_directory(user) -> None:
    """
    Make annotation directory of the user

    Args:
        user (str): Name of the current user annotator
    """
    user_path = os.path.join(ANNOTATED, user)
    os.mkdir(user_path)


def get_videos() -> list:
    """
    Get the total videos in the database

    Returns:
        list: List of the Videos
    """
    return os.listdir(VIDEOS)


def num_videos() -> int:
    """
    Get the total number of the videos in the database

    Returns:
        int: Number of the total videos in the database
    """
    return len(get_videos())


def annotated(username) -> list:
    """
    Get the annotated video names of the current user

    Args:
        username (str): User name of the current annotator

    Returns:
        list: List of the video names
    """

    name = os.path.join(ANNOTATED, username + '.txt')
    return read_txt(name)


def num_annotated(username) -> int:
    """
    Total number of annotated videos from the current username

    Args:
        username (str): User name annotator

    Returns:
        int: Number of total annotated videos
    """
    return len(annotated(username))


def read_txt(path) -> list:
    """
    Reading the txt file line by line

    Args:
        path (str): Path name of the txt file to read

    Returns:
        list: List of the data from the text file
    """
    with open(path, 'r') as f:
        data = [line.split('\n')[0] for line in f.readlines()]
    return data


def get_difference(username) -> list:
    """
    Get the between the total videos and the annotated videos of the current user.

    Args:
        username (str): User name of the current user

    Returns:
        list: List of the videos that have not been annotated from the current user
    """
    diff = list(set(get_videos()) - set(annotated(username)))

    return diff


def get_random_video(diff) -> str:
    """
    Get a random video to be annotated

    Args:
        diff (list): List of the videos that have not been annotated from the current user

    Returns:
        str: File name of the random video to be annotated
    """
    return random.choice(diff)


def add_annotation(user, video, data) -> None:
    """
    Save annotations to the csv file for the current user.

    Args:
        user (str): User name of the current user
        video (str): Video name to be annotated
        data (list): List of the annotated timestamps for the specific video
    """
    dirname = os.path.join(ANNOTATED, user)
    video_path = os.path.join(dirname, video + '.csv')
    df = pd.DataFrame(data=data, columns=['Start Minutes', 'Start Seconds', 'End Minutes', 'End Seconds'])
    df.to_csv(video_path, index=False)


def create_directories():
    """
    Check if the directories exists, otherwise it creates the VIDEOS and ANNOTATED directories.
    """
    if not os.path.isdir(ANNOTATED):
        os.mkdir(ANNOTATED)
    if not os.path.isdir(VIDEOS):
        os.mkdir(VIDEOS)
