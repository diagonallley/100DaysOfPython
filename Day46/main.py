from bs4 import BeautifulSoup
import requests
from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pyperclip
import json
import os

SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
print(SPOTIFY_CLIENT_ID)
print(SPOTIFY_CLIENT_SECRET)
# TIME_MACHINE
date = None
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
if date == None or date == "":
    date = "2010-10-20"

play_list_uri = ""
playlist__="hot-100"
URL = "https://www.billboard.com/charts/hot-100/"


def scrape_songs(date):
    billboard_hot = requests.get(URL+date)

    billboard_hot.raise_for_status()

    soup = BeautifulSoup(billboard_hot.text, "html.parser")

    songs = soup.find_all("div", class_='o-chart-results-list-row-container')

    songs_list = []
    # songs_list = [{(song.find("h3", id="title-of-a-story").get_text().strip())
    #                 : (song.find_all("span")[1].get_text().strip())} for song in songs]

    for song in songs:
        song_title = song.find("h3", id="title-of-a-story").get_text().strip()
        song_artist = song.find_all(
            "span", class_="a-no-trucate")[0].get_text().strip()

        songs_list.append({song_title: song_artist})

    return songs_list


# pprint(songs_list)
scope = "playlist-modify-private"


def authenticate_login(scope="user-top-read"):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                         client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri="https://github.com/diagonallley", scope=scope))
    return sp


def get_curent_user(sp):
    current_user = sp.current_user()["id"]
    return current_user


def make_playlist(date, sp, user="31o4bq5l7gendnb6n2d43yiufu3m"):
    name_of_playlist = f"{date}-BILLBOARD 100"
    description = f"Get back to {date.split('-')[0]}s"
    playlist = sp.user_playlist_create(
        user=user, name=name_of_playlist, public=False, collaborative=False, description=description)
    return playlist


SP_USER = os.environ.get("SP_USER")


def add_to_playlist(sp, date, songs_list, play_list_uri):
    year = date.split("-")[0]
    list_of_song_uris = []
    for s in songs_list:
        for song, artist in s.items():
            result = sp.search(q=f"track:{song} year:{year}", type="track")
            try:
                song_uri = result["tracks"]["items"][0]["uri"]
                list_of_song_uris.append(song_uri)
            except IndexError:
                print("Song not found")

            # pyperclip.copy(json.dumps(result))
    sp.user_playlist_add_tracks(user=SP_USER,
                                playlist_id=play_list_uri, position=None, tracks=list_of_song_uris)


def get_top_artists_tracks(sp):
    top_artists = sp.current_user_top_artists(limit=20)
    top_tracks = sp.current_user_top_tracks(limit=20)
    return (top_artists, top_tracks)


def get_special_features(top_tracks):
    special_ = sp.audio_features(tracks=[top_tracks["items"][0]["uri"]])
    return special_


# STEP 1: Scrape the songs for the given date:

songs_list = scrape_songs(date=date)

pprint(songs_list)

# STEP 2:
sp = authenticate_login(scope=scope)

# STEP 3: Make a playlist with the date, take the id of the playlist from the date
# playlist = make_playlist(date, sp=sp)  # user=optional

playlist = ""
pyperclip.copy(json.dumps(playlist))

# STEP
add_to_playlist(sp=sp, date=date, songs_list=songs_list,
                play_list_uri=playlist)
