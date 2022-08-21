#!/usr/bin/env python3
'''
    Convert Spotify playlist 2 csv
    Created by argv1
'''
import argparse
from configparser import ConfigParser
import pandas as pd
from   pathlib import Path
import re
import spotipy
import spotipy.util as util

# Global settings
base_path = Path(__file__).parent.absolute()
playlists = base_path / "playlists"
config_file = ConfigParser()
config_file.read(base_path / 'config.ini')
SPOTIFY_USERNAME = config_file['AUTH']['SPOTIFY_USERNAME']
SPOTIFY_CLIENT_ID = config_file['AUTH']['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = config_file['AUTH']['SPOTIFY_CLIENT_SECRET']
spotify_scope = "playlist-read-private" 
token = util.prompt_for_user_token(username=SPOTIFY_USERNAME, scope=spotify_scope, client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri='http://localhost:8888/callback')
sp = spotipy.Spotify(auth=token)


def get_playlist_id(playlist_link):
    if match := re.match(r"https://open.spotify.com/playlist/(.*)\?", playlist_link):
        playlist_url = match.groups()[0]
    else:
        raise ValueError("Expected format: https://open.spotify.com/playlist/...")

    # get list of tracks in a given playlist (note: max playlist length 100)
    return(sp.playlist_tracks(playlist_url)["items"])

def generate_playlist(tracks, playlist): 
    # Get every title and artist
    titles, artists = [], []
    for track in tracks:
        titles.append(track["track"]["name"])
        artists.append(", ".join([artist["name"] for artist in track["track"]["artists"]]))
    
    playlist_dict = {"Title": titles, "artists": artists}

    # create pandas dataframe
    df = pd.DataFrame.from_dict(playlist_dict)

    #check for duplicates
    print(f"Duplicate entries in the playlist found: {len(df[df.duplicated()])}")

    # write to csv
    df.dropna(axis=0, inplace=True)
    df.to_csv(f"{playlists}/{playlist}.csv", index=True, sep=";", encoding="iso-8859-1")


def main():
    # Initiate the parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--playlist', help='Enter the the name for the saved csv file', type=str, required=True)
    parser.add_argument('-u', '--url', help='Enter the url of the spotify playlist that should be scrapped', type=str, required=True)    
    args = parser.parse_args()

    # Lookup for playlist
    tracks = get_playlist_id(args.url)

    # Convert to csv
    generate_playlist(tracks, args.playlist)
        
if __name__  == "__main__":
    main()