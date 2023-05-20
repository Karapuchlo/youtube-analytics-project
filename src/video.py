import requests
class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        self.title = None
        self.description = None
        self.views = None
        self.like_count = None
        try:
            # использование API для получения данных о видео по его ID
            response = requests.get(f"https://api.example.com/videos/{video_id}")
            data = response.json()
            if "items" not in data or not data["items"]:
                raise Exception("Empty or invalid response from API.")
            snippet = data["items"][0].get("snippet")
            if not snippet:
                raise Exception("Incomplete data.")
            self.title = snippet.get("title")
            self.description = snippet.get("description")
            statistics = data["items"][0].get("statistics")
            if not statistics:
                raise Exception("Incomplete data.")
            self.views = statistics.get("viewCount")
            self.like_count = statistics.get("likeCount")
        except requests.exceptions.RequestException:
            print(f"Failed to fetch data for video id {video_id}.")
        except KeyError:
            print(f"Data for video id {video_id} is incomplete.")
        except IndexError:
            print(f"No data found for video id {video_id}.")
        except Exception as e:
            print(f"Unexpected error while fetching data for video id {video_id}: {e}.")
            self.video_id = None
            self.title = None
            self.description = None
            self.views = None
            self.like_count = None