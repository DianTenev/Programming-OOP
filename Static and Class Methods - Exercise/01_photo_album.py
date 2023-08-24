import math


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label):
        for index, page in enumerate(self.photos):
            if len(page) < 4:
                page.append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(page)}"
        else:
            return "No more free slots"

    def display(self):
        res = "-" * 11 + "\n"
        for row in self.photos:
            res += " ".join(["[]" for _ in row]) + "\n"
            res += "-" * 11 + "\n"
        return res


album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())
