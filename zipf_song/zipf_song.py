from typing import List, Tuple

# represent a list of tuple where int is the number of time a song is listened, and the string the title of the song.
SongList = List[Tuple[int, str]]


def zipf_algo(zif_number_reference: int):
    def in_sorting(position: int, song_listened_number: int):
        return song_listened_number / (zif_number_reference / position)

    return in_sorting


def zipf_song(song_selected: int, song_list: SongList):
    sorting_zipf = zipf_algo(song_list[0][0])
    sorted_song_list = sorted(song_list, key=lambda s: sorting_zipf(song_list.index(s) + 1, s[0]), reverse=True)
    return sorted_song_list[:song_selected]
