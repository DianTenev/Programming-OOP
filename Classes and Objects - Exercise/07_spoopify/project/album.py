from project.song import Song
from typing import List, Tuple


class Album:
    def __init__(self, name: str, *songs: Tuple[Song]):
        self.name = name
        self.published: bool = False
        self.songs: List[Song] = [*songs]

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."

        try:
            song = next(filter(lambda x: x.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        self.songs.remove(song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        album_info = "\n".join([f"== {current_song.get_info()}" for current_song in self.songs])
        return f"Album {self.name}\n" \
               f"{album_info}" \
               f"\n"

