import os
import pygame


class MusicPlayer:
    def __init__(self, music_folder="music"):
        pygame.mixer.init()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.music_folder = os.path.join(base_dir, music_folder)

        self.playlist = self.load_tracks()
        self.current_index = 0

        self.is_playing = False
        self.is_paused = False
        self.stopped_manually = False

    def load_tracks(self):
        tracks = []

        if not os.path.exists(self.music_folder):
            return tracks

        for file_name in os.listdir(self.music_folder):
            if file_name.lower().endswith((".mp3", ".wav", ".ogg")):
                tracks.append(file_name)

        tracks.sort()
        return tracks

    def get_total_tracks(self):
        return len(self.playlist)

    def get_current_track_path(self):
        if self.get_total_tracks() == 0:
            return None
        return os.path.join(self.music_folder, self.playlist[self.current_index])

    def get_track_name(self):
        if self.get_total_tracks() == 0:
            return "No track"
        return self.playlist[self.current_index]

    def get_status(self):
        if self.get_total_tracks() == 0:
            return "No tracks"
        if self.is_paused:
            return "Paused"
        if self.is_playing:
            return "Playing"
        return "Stopped"

    def get_position_seconds(self):
        if not self.is_playing and not self.is_paused:
            return 0

        pos_ms = pygame.mixer.music.get_pos()

        if pos_ms < 0:
            return 0

        return pos_ms // 1000

    def play(self):
        if self.get_total_tracks() == 0:
            return

        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.is_playing = True
            self.stopped_manually = False
            return

        track_path = self.get_current_track_path()
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()

        self.is_playing = True
        self.is_paused = False
        self.stopped_manually = False

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        self.stopped_manually = True

    def pause_resume(self):
        if self.get_total_tracks() == 0:
            return

        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.is_playing = False
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.is_playing = True
            self.stopped_manually = False

    def next_track(self):
        if self.get_total_tracks() == 0:
            return

        self.current_index = (self.current_index + 1) % self.get_total_tracks()
        self.play()

    def prev_track(self):
        if self.get_total_tracks() == 0:
            return

        self.current_index = (self.current_index - 1) % self.get_total_tracks()
        self.play()

    def update(self):
        if self.get_total_tracks() == 0:
            return

        if self.is_playing and not self.is_paused:
            if not pygame.mixer.music.get_busy():
                if not self.stopped_manually:
                    self.current_index = (self.current_index + 1) % self.get_total_tracks()
                    self.play()