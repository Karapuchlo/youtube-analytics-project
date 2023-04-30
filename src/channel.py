from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json

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
    def get_service(cls):
        if not cls._service:
            credentials = Credentials.from_authorized_user_file('kuplinov.json',
                                                                ['https://www.googleapis.com/auth/youtube.readonly'])
            cls._service = build('youtube', 'v3', credentials=credentials)
        return cls._service

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
