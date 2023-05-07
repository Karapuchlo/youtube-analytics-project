class Video:
    def __init__(self, video_id):
        self.video_id = video_id



class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id