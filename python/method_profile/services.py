from engine import InstagramScraper
from extractor import Extractor
from whatap import method_profiling
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
@method_profiling
def get_top_posts_success(hashtag):

    logger.info(f"hashtag:{hashtag} 인기 게시물 수집")

    logger.info(f"크롤링 시작")
    scraper = InstagramScraper(logger)
    raw_data = scraper.get_raw_instagram_hashtag(hashtag)
    logger.info(f"크롤링 완료")
    logger.info(f"파싱 시작")
    extractor = Extractor()
    data = extractor.extract_hashtag(raw_data)
    logger.info(f"파싱 완료")

    logger.info(f"데이터 추가 시작")
    for post in data.top_posts:
        with open(file=f"share/data.csv", mode="a+") as f:
            f.seek(0)
            text_append = f"{data.name}\t{post.caption}\t{post.like_count}\t{post.comment_count}\t{post.hashtags}\t{post.shortcode}\t{post.url}\t{post.taken_at_timestamp}"

            if f.read():
                ### 내용이 존재하면 받아온값을 추가해준다.
                f.write(f"\n{text_append}")

            else:
                ### 내용이 존재하지 않으면 칼럼을 먼저 추가하고 내용을 추가한다.
                f.write(f"hashtag\tcaption\tlike_count\tcomment_count\trelated_tags\tshortcode\turl\ttimestamp")
                f.write(f"\n{text_append}")
    logger.info(f"데이터 추가 완료")
    logger.info(f"해시태그:{hashtag}에 대한 인기 게시물 수집 완료")

@method_profiling
def get_top_posts_error(hashtag):
    logger.info(f"해시태그:{hashtag} 인기 게시물 수집")

    logger.info(f"크롤링 시작")

    scraper = InstagramScraper(logger)

    raw_data = scraper.get_raw_instagram_hashtag(hashtag+"!@#")
    logger.info(f"크롤링 완료")
    logger.info(f"파싱 시작")
    extractor = Extractor()
    data = extractor.extract_hashtag(raw_data)

    logger.info(f"파싱 완료")
    logger.info(f"데이터 추가 시작")
    for post in data.top_posts:
        with open(file=f"share/data.csv", mode="a+") as f:
            f.seek(0)
            text_append = f"{data.name}\t{post.caption}\t{post.like_count}\t{post.comment_count}\t{post.hashtags}\t{post.shortcode}\t{post.url}\t{post.taken_at_timestamp}"

            if f.read():
                ### 내용이 존재하면 받아온값을 추가해준다.
                f.write(f"\n{text_append}")
            else:
                ### 내용이 존재하지 않으면 칼럼을 먼저 추가하고 내용을 추가한다.
                f.write(f"hashtag\tcaption\tlike_count\tcomment_count\trelated_tags\tshortcode\turl\ttimestamp")
                f.write(f"\n{text_append}")
    logger.info(f"데이터 추가 완료")
    logger.info(f"해시태그:{hashtag}에 대한 인기 게시물 수집 완료")