def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order
             in which they were chosen.
    """

    result = []
    current_size = 0
    first_song = songs[0]
    work_songs = sorted(songs[:], key = lambda item: item[2])
    # print(work_songs)
    # print(songs)
    if max_size > first_song[2]:
        result.append(first_song[0])
        current_size += first_song[2]
        work_songs = [i for i in work_songs if i[0] != first_song[0]]
    else:
        return result
    for song in work_songs:
        if song[2] + current_size <= max_size:
            result.append(song[0])
            current_size += song[2]
            work_songs = [i for i in work_songs if i[0] != song[0]]

    return result


    print(result)
    print(work_songs)



list1 = [('Roar',4.4, 4.0),('Sail',3.5, 7.7),('Timber', 5.1, 6.9),('Wannabe',2.7, 1.2)]


song_playlist(list1, 11)
