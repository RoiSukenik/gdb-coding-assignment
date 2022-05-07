import json
import os
import time
from typing import Optional, List

import requests
from dotenv import load_dotenv
from oauthlib.oauth2 import BackendApplicationClient
from pydantic.main import BaseModel
from requests_oauthlib import OAuth2Session

import constants as constant

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET")


class FeaturedSong(BaseModel):
    track_id: str
    track_name: str
    playlist_id: str
    playlist_name: str
    album_name: Optional[str]
    album_tracks: Optional[int]
    # if this track is part of an album, this number represents how many tracks there are in the album
    artist_names: List[str]

    playlist_rank: int  # position of the playlist in the api results
    track_rank: int  # position of the track in the playlist


def get_auth_response():
    client = BackendApplicationClient(client_id=SPOTIFY_CLIENT_ID)
    oauth = OAuth2Session(client=client)
    auth_resp = oauth.fetch_token(token_url='https://accounts.spotify.com/api/token', client_secret=SPOTIFY_SECRET)
    return auth_resp


def map_to_artiest_names_list(artiest_object) -> List[str]:
    return artiest_object["name"]


def track_to_featured_song(track_obj: dict, playlist_id: str, playlist_name: str, playlist_rank: int,
                           track_rank: int) -> FeaturedSong:
    track = track_obj["track"]
    if track is None:
        return None
    artiest_list = list(map(map_to_artiest_names_list, track["artists"]))
    featured_song = FeaturedSong(track_id=track["id"], track_name=track["name"], artist_names=artiest_list,
                                 playlist_id=playlist_id, playlist_name=playlist_name,
                                 playlist_rank=playlist_rank + constant.RANKING_ADJUSTER,
                                 track_rank=track_rank + constant.RANKING_ADJUSTER)
    return featured_song


def get_playlist_tracks(access_token: str, playlist_item: dict):
    url = playlist_item["tracks"]["href"].replace("/tracks", "")
    playlist = requests.request(method="GET",
                                url=url,
                                headers={"Authorization": f"Bearer {access_token} "})
    if playlist.status_code != 200:
        raise Exception(playlist.error.message)

    track = json.loads(playlist.text)
    return track["tracks"]["items"]


def get_playlists_by_category(access_token: str, category: str, country_code: str):
    response = requests.request(method="GET", url=f"https://api.spotify.com/v1/browse/categories/{category}/playlists",
                                headers={"Authorization": f"Bearer {access_token} "},
                                params={"country": country_code, "limit": constant.PLAYLIST_LIMIT})

    if response.status_code != 200:
        raise Exception(response.error.message)
    return json.loads(response.text)


def track_data(category: str, country_code: str) -> List[FeaturedSong]:
    access_token = get_auth_response()["access_token"]

    playlists = get_playlists_by_category(access_token, category, country_code)["playlists"]["items"]
    featured_songs = list()
    for playlist_index in range(len(playlists)):
        playlist_tracks = get_playlist_tracks(access_token, playlists[playlist_index])
        for track_index in range(len(playlist_tracks)):
            featured_song = track_to_featured_song(playlist_tracks[track_index], playlists[playlist_index]["id"],
                                                   playlists[playlist_index]["name"], playlist_index, track_index)
            if featured_song is None:
                continue

            featured_songs.append(featured_song)

    return featured_songs


if __name__ == '__main__':
    timer = time.time()
    result_logs = track_data('pop', 'US')
    time_took = time.time() - timer
    assert result_logs and isinstance(result_logs, list)
    assert all([isinstance(log, FeaturedSong) for log in result_logs])
    print(f'Track complete, produced {len(result_logs)} logs and took {time_took:.5} seconds')
