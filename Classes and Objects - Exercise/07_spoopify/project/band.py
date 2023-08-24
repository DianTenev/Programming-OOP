from project.song import Song
from project.album import Album
from typing import List


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
            album = next(filter(lambda x: x.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."
        if album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(album)
        return f"Album {album_name} has been removed."

    def details(self):
        band_info = "\n".join([f"{current_album.details()}" for current_album in self.albums])
        return f"Band {self.name}\n" \
               f"{band_info}"


song = Song("Fight back", 3.21, False)
print(song.get_info())
album = Album("Fight back: The collection", song)
second_song = Song("Soldier", 3.36, False)
third_song = Song("Make it", 4.13, False)
fourth_song = Song("Never give up", 4.11, False)
fifth_song = Song("Failure", 5.17, False)
sixth_song = Song("Spartan", 2.33, False)
print(album.add_song(second_song))
print(album.add_song(third_song))
print(album.add_song(fourth_song))
print(album.add_song(fifth_song))
print(album.add_song(sixth_song))
print()
print(album.details())
print()
print(album.publish())
destiny_song = Song("Destiny", 3.26, False)
second_album = Album("Destiny: The collection", destiny_song)
destiny_second_song = Song("Cold", 3.06, False)
destiny_third_song = Song("Cold in the water", 2.44, False)
destiny_fourth_song = Song("Life", 2.08, False)
print(second_album.add_song(destiny_song))
print(second_album.add_song(destiny_second_song))
print(second_album.add_song(destiny_third_song))
print(second_album.add_song(destiny_fourth_song))
print(second_album.publish())
band = Band("NEFFEX")
print(band.add_album(album))
print(band.add_album(second_album))
print(band.remove_album("Initial D"))
print()
print(band.details())



