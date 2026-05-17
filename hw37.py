class AudioFileMixin:
    def play_audio(self):
        if not hasattr(self, "audio_tracks"):
            raise AttributeError("Absent audio_tracks")
        tracks = "\n".join(self.audio_tracks)
        return f"Audio playback for {self.__class__.__name__}:\n{tracks}"

class VideoFileMixin:
    def play_video(self):
        if not hasattr(self, 'video_files'):
            raise AttributeError("Absent video_files")
        videos = "\n".join(self.video_files)
        return f"Video playback for {self.__class__.__name__}:\n{videos}"

class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks


class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files):
        self.audio_tracks = audio_tracks
        self.video_files = video_files


tracks = ["track1.mp3", "track2.mp3"]
movies = ["movie.mp4", "trailer.mov"]

player = MediaPlayer(tracks)
print(player.play_audio())
laptop = Laptop(tracks, movies)
print(laptop.play_audio())
print(laptop.play_video())