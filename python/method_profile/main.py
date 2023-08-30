from services import get_top_posts_success, get_top_posts_error
import time
import os
time.sleep(3)

hashtag = os.getenv("HASHTAG")
get_top_posts_success(hashtag)
get_top_posts_error(hashtag)
time.sleep(7200)


