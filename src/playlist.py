from datetime import datetime, timedelta
import os
from googleapiclient.discovery import build
class PlayList:
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        # Получение названия и URL плейлиста, например, используя YouTube API:
        self.title = self.get_playlist_title()
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'
        self.videos = self.get_playlist_videos()

    def get_playlist_videos(self):
        api_key = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        videos = []
        next_page_token = None
        # Проходим по всем страницам и собираем список видео:
        while True:
            playlist_items = youtube.playlistItems().list(part='snippet', playlistId=self.playlist_id,
                                                          maxResults=50, pageToken=next_page_token).execute()
            video_ids = []
            for item in playlist_items['items']:
                video_id = item['snippet']['resourceId']['videoId']
                video_ids.append(video_id)
            videos.extend(self._get_videos_metadata(video_ids))
            next_page_token = playlist_items.get('nextPageToken')
            if not next_page_token:
                break
        return videos

    def get_playlist_title(self):
        api_key = os.getenv('API_KEY')

        youtube = build('youtube', 'v3', developerKey=api_key)
        playlist = youtube.playlists().list(part='snippet', id=self.playlist_id).execute()
        title = playlist['items'][0]['snippet']['title']
        return title


    def _get_videos_metadata(self, video_ids):
        api_key = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        metadata = []
        for i in range(0, len(video_ids), 50):
            videos = youtube.videos().list(id=','.join(video_ids[i:i + 50]), part='snippet,contentDetails, statistics').execute()

            for video in videos['items']:
                video_id = video['id']
                title = video['snippet']['title']
                thumbnail = video['snippet']['thumbnails']['high']['url']
                duration = video['contentDetails']['duration']
                url = f'https://www.youtube.com/watch?v={video_id}'
                likes = video['statistics']['likeCount']
                metadata.append({'id': video_id, 'title': title, 'thumbnail': thumbnail, 'url': url, 'duration': duration, 'likes': likes})

        return metadata

    @property
    def total_duration(self):
        total = timedelta()
        for video in self.videos:
            duration = datetime.strptime(video['duration'], "PT%MM%SS") - datetime(1900, 1, 1)
            total += timedelta(minutes=duration.total_seconds() // 60, seconds=duration.total_seconds() % 60)
        return total

    def show_best_video(self):
        best_video = None
        max_likes = 0
        for video in self.videos:
            if int(video.get('likes', 0)) > int(max_likes):
                max_likes = video['likes']
                best_video = video['url']
        return best_video

    def __str__(self):
        return f"{self.title}"