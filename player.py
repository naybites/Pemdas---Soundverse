class Player:
    def __init__(self, music_library, audio_player):
        self.music_library = music_library
        self.audio_player = audio_player
        self.current_song_index = 0
        self.is_playing = False

    def play(self):
        if self.music_library.get_song_list():
            song = self.music_library.get_song_list()[self.current_song_index]
            self.audio_player.play(song)
            self.is_playing = True

    def pause(self):
        self.audio_player.pause()
        self.is_playing = False

    def stop(self):
        self.audio_player.stop()
        self.is_playing = False

    def next_song(self):
        if self.music_library.get_song_list():
            self.current_song_index = (self.current_song_index + 1) % len(self.music_library.get_song_list())
            self.play()

    def previous_song(self):
        if self.music_library.get_song_list():
            self.current_song_index = (self.current_song_index - 1) % len(self.music_library.get_song_list())
            self.play()

    def shuffle(self):
        import random
        random.shuffle(self.music_library.songs)
        self.current_song_index = 0
        self.play()