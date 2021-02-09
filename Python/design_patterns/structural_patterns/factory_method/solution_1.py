import json
import xml.etree.ElementTree as et


# class Song:
#     def __init__(self, song_id, title, artist):
#         self.song_id = song_id
#         self.title = title
#         self.artist = artist
#
#
# class SongSerializer:
#     def serialize(self, song, format):
#         if format == "JSON":
#             song_info = {"id": song.song_id, "title": song.title, "artist": song.artist}
#             return json.dumps(song_info)
#         elif format == "XML":
#             song_info = et.Element("song", attrib={"id": song.song_id})
#             title = et.SubElement(song_info, "title")
#             title.text = song.title
#             artist = et.SubElement(song_info, "artist")
#             artist.text = song.artist
#             return et.tostring(song_info, encoding="unicode")
#         else:
#             raise ValueError(format)


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


class SongSerializer:
    # Client
    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        return serializer(song)

    # Creator component
    # the component chooses which implementation to use
    #
    # The creator returns the concrete implementation
    # according to the value of the parameter to the client,
    # and the client uses the provided object to complete its task.
    def _get_serializer(self, format):
        if format == "JSON":
            return self._serialize_to_json
        elif format == "XML":
            return self._serialize_to_xml
        else:
            raise ValueError(format)

    # an Product implementation
    def _serialize_to_json(self, song):
        song_info = {"id": song.song_id, "title": song.title, "artist": song.artist}
        return json.dumps(song_info)

    # an Product implementation
    def _serialize_to_xml(self, song):
        song_info = et.Element("song", attrib={"id": song.song_id})
        title = et.SubElement(song_info, "title")
        title.text = song.title
        artist = et.SubElement(song_info, "artist")
        artist.text = song.artist
        return et.tostring(song_info, encoding="unicode")


if __name__ == "__main__":
    song = Song("1", "Shape Of My Heart", "Sting")
    serializer = SongSerializer()

    print(serializer.serialize(song, "JSON"))
    print(serializer.serialize(song, "XML"))
    print(serializer.serialize(song, "YAML"))
