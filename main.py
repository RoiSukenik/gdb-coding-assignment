import time
from typing import Optional, List

from pydantic.main import BaseModel


class FeaturedSong(BaseModel):
    track_id: str
    track_name: str
    playlist_id: str
    playlist_name: str
    album_name: Optional[str]
    album_tracks: Optional[int]. # if this track is part of an album, this number represents how many tracks there are in the album
    artist_names: List[str]

    playlist_rank: int  # position of the playlist in the api results
    track_rank: int  # position of the track in the playlist


def track_data(category: str, country_code: str) -> List[FeaturedSong]:
    # TODO: add your implementation here. implement & call other methods as necessary
    raise NotImplementedError


if __name__ == '__main__':
    timer = time.time()
    result_logs = track_data('pop', 'US')
    time_took = time.time() - timer
    assert result_logs and isinstance(result_logs, list)
    assert all([isinstance(log, FeaturedSong) for log in result_logs])
    print(f'Track complete, produced {len(result_logs)} logs and took {time_took:.5} seconds')
