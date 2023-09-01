from services import get_top_posts
import time
import os
time.sleep(3)

hashtag = os.getenv("HASHTAG")
get_top_posts(hashtag)
time.sleep(300)


