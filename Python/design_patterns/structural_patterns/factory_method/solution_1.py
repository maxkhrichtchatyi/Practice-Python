import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    def serialize(self, song, format):
        if format == "JSON":
            song_info = {"id": song.song_id, "title": song.title, "artist": song.artist}
            return json.dumps(song_info)
        elif format == "XML":
            song_info = et.Element("song", attrib={"id": song.song_id})
            title = et.SubElement(song_info, "title")
            title.text = song.title
            artist = et.SubElement(song_info, "artist")
            artist.text = song.artist
            return et.tostring(song_info, encoding="unicode")
        else:
            raise ValueError(format)


if __name__ == "__main__":
    song = Song("1", "Shape Of My Heart", "Sting")
    serializer = SongSerializer()

    print(serializer.serialize(song, "JSON"))
    print(serializer.serialize(song, "XML"))
    print(serializer.serialize(song, "YAML"))
