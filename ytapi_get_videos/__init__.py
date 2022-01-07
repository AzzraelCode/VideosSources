import datetime
import json

from googleapiclient.discovery import build

from _creds import yt_api_key as API_KEY


def main():
    """
    https://developers.google.com/youtube/v3/docs/search/list
    :return:
    """
    print('YouTube API Получаю свежие видео на канале')

    # channelId = "UCf6kozNejHoQuFhBDB8cfxA"
    channelId = "UCQfwKTJdCmiA6cXAY0PNRJw"

    service = build('youtube', 'v3', developerKey=API_KEY)

    r = service.search().list(
        channelId=channelId,
        part="snippet",
        type='video',
        order='rating',
        maxResults="15",
        # publishedAfter=datetime.datetime(2021, 1, 1, 0, 0, tzinfo=datetime.timezone.utc).isoformat(),
        # publishedBefore=datetime.datetime(2022, 1, 1, 0, 0, tzinfo=datetime.timezone.utc).isoformat()
    ).execute()

    # print(json.dumps(r))

    print(f"nextPageToken {r['nextPageToken']}")
    [print("%s, %s, https://youtu.be/%s" % (item['snippet']['title'], item['snippet']['publishedAt'], item['id']['videoId'])) for item in r['items']]