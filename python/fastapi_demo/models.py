from typing import List, Optional
from pydantic import BaseModel, HttpUrl

class Result(BaseModel):
    hashtag: Optional[str]
    caption: Optional[str]
    like_count: Optional[int]
    comment_count: Optional[int]
    related_tags: List[str] = []
    shortcode: Optional[str]
    url: Optional[HttpUrl]
    timestamp: Optional[int]
