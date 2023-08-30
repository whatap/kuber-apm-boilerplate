import re
from datetime import datetime, timezone, timedelta
from utils import json_value
from models import HashtagPost, Hashtag

class Extractor:
    def _extract_hashtag_post(self, data: dict):
        hashtagpost = {
            'id': json_value(data, "node", "id"),
            'shortcode': json_value(data, "node", "shortcode"),
            # 'owner_id': json_value(data, "node", "owner", "id"),
            'like_count': json_value(data, "node", "edge_liked_by", "count"),
            'comment_count': json_value(data, "node", "edge_media_to_comment", "count"),
            'taken_at_timestamp': json_value(data, "node", "taken_at_timestamp"),
            'caption': json_value(data, "node", "edge_media_to_caption", "edges", 0, "node", "text"),
            'display_url': json_value(data, "node", "display_url"),
            'thumbnail_url': json_value(data, "node", "thumbnail_src"),
            "is_video": json_value(data, "node", "is_video"),
            "media_type": json_value(data, "node", "__typename")
        }

        hashtagpost['url'] = self._extract_url_from_shortcode(hashtagpost['shortcode'])
        hashtagpost['created_at'] = self._extract_datetime_from_timestamp(hashtagpost['taken_at_timestamp'])
        hashtagpost['hashtags'] = self._extract_hashtags_from_text(hashtagpost['caption'])
        if hashtagpost.get('caption'):
            hashtagpost['caption'] = hashtagpost['caption'].replace("\n", "")
        try:
            data = HashtagPost(**hashtagpost)
        except Exception as e:
            raise e
        else:
            return data

    def _extract_hashtags_from_text(self, text: str):
        _REGEX_HASHTAG = re.compile(r"(?:#)(\w(?:(?:\w|(?:\.(?!\.))){0,28}(?:\w))?)")
        try:
            return list(set(re.findall(_REGEX_HASHTAG, text)))
        except Exception as ex:
            return []

    def _extract_datetime_from_timestamp(self, timestamp: int, tz_hours: int = 0):
        return datetime.fromtimestamp(timestamp, tz=timezone(timedelta(hours=tz_hours)))

    def _extract_url_from_shortcode(self, shortcode: str):
        return "https://www.instagram.com/p/%s" % shortcode

    def extract_hashtag(self, raw_data: dict):
        hashtag = {
            'raw_data': raw_data,
            'id': json_value(raw_data, "data", "hashtag", "id"),
            'name': json_value(raw_data, "data", "hashtag", "name"),
            'media_count': json_value(raw_data, "count"),
            'profile_pic_url': json_value(raw_data, "data", "hashtag", "profile_pic_url"),
            'related_tags': json_value(raw_data, "data", "hashtag", "edge_hashtag_to_related_tags", "edges")
        }
        hashtag_top_posts = json_value(raw_data, "data", "hashtag", "edge_hashtag_to_top_posts", "edges")
        hashtag_recent_posts = json_value(raw_data, "data", "hashtag", "edge_hashtag_to_media", "edges")

        hashtag['top_posts'] = [self._extract_hashtag_post(post) for post in hashtag_top_posts]
        hashtag['recent_posts'] = [self._extract_hashtag_post(post) for post in hashtag_recent_posts]

        try:
            data = Hashtag(**hashtag)
        except Exception as e:
            raise e
        else:
            return data