import os
from googleapiclient.discovery import build
class Video:

    def __init__(self, video_id, duration):
        self.video_id = video_id
        api_key = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        video = youtube.videos().list(part='snippet,statistics,contentDetails', id=video_id).execute()['items'][0]['snippet']
        try:
            self.duration = duration

            self.title = video['title']
            self.url = f"https://www.youtube.com/watch?v={video_id}"
       # self.views = video['statistics']['viewCount']
       # self.likes = video['statistics']['likeCount']
        except requests.exceptions.RequestException:
            print(f"Failed to fetch data for video id {video_id}.")
        except KeyError:
            print(f"Data for video id {video_id} is incomplete.")
        except Exception as e:
            print(f"Unexpected error while fetching data for video id {video_id}: {e}.")

    def __str__(self):
        return f"{self.title}"


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f"{super().__str__()}"