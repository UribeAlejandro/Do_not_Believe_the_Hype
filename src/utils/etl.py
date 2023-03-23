import json
import os
from glob import glob
from typing import List

import lyricsgenius as genius
from dotenv import load_dotenv

load_dotenv()
GENIUS_API_KEY = os.getenv("GENIUS_API_KEY")


def download_artist_lyrics(artist: str) -> List[str]:
    api = genius.Genius(GENIUS_API_KEY)
    artist = api.search_artist(
        "arctic monkeys", sort="title", include_features=False
    )
    lyrics = artist.save_lyrics()

    lyrics = []
    for f_name in glob("./*.json"):
        config = json.loads(open(f_name).read())
        lyrics.append(config)


def _download_lyrics():
    ...
