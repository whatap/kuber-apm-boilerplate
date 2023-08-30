from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class HashtagPost(BaseModel):
    id: str
    shortcode: str
    url: Optional[HttpUrl]
    # owner_id: Optional[int]
    # owner_name: Optional[str]
    taken_at_timestamp: Optional[int]
    created_at: Optional[datetime]
    like_count: int
    comment_count: int
    caption: Optional[str]
    hashtags: List[str] = []
    display_url: Optional[HttpUrl]
    thumbnail_url: Optional[HttpUrl]
    is_video: Optional[bool]
    media_type: Optional[str]

class Hashtag(BaseModel):
    id: str
    name: str
    media_count: Optional[int]
    profile_pic_url: Optional[HttpUrl]
    related_tags: Optional[List[str]]
    top_posts: List[HashtagPost] = []
    recent_posts: List[HashtagPost] = []
    raw_data: dict
