from googleapiclient.discovery import build
import json
import os
ap_key: str = os.getenv('API_KEY')
class Channel:
    _service = None

    def __init__(self, channel_id):
        self._channel_id = channel_id

        youtube = self.get_service()
        request = youtube.channels().list(
            part="snippet,statistics",
            id=channel_id
        )
        response = request.execute()
        item = response['items'][0]

        self._title = item['snippet']['title']
        self._description = item['snippet']['description']
        self._url = f"https://www.youtube.com/channel/{channel_id}"
        self._subscribers = int(item['statistics']['subscriberCount'])
        self._video_count = int(item['statistics']['videoCount'])
        self._view_count = int(item['statistics']['viewCount'])

    @classmethod
    def get_service(self):
        return build('youtube', 'v3', developerKey=ap_key)

    def __str__(self):
        return f"{self._title} ({self._url})"

    def __add__(self, other):
        if isinstance(other, Channel):
            return self._subscribers + other._subscribers

    def __sub__(self, other):
        if isinstance(other, Channel):
            return self._subscribers - other._subscribers

    def __lt__(self, other):
        return self._subscribers < other._subscribers

    def __gt__(self, other):
        return self._subscribers > other._subscribers

    def __eq__(self, other):
        return self._subscribers == other._subscribers

    @property
    def channel_id(self):
        return self._channel_id

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def url(self):
        return self._url

    @property
    def subscribers(self):
        return self._subscribers

    @property
    def video_count(self):
        return self._video_count

    @property
    def view_count(self):
        return self._view_count

    def to_json(self, filename):
        data = {
            "channel_id": self._channel_id,
            "title": self._title,
            "description": self._description,
            "url": self._url,
            "subscribers": self._subscribers,
            "video_count": self._video_count,
            "view_count": self._view_count
        }
        with open(filename, "w") as file:
            json.dump(data, file)
