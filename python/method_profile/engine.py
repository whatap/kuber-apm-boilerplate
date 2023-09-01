import json
import time
import requests
from exceptions import *
from extractor import Extractor
class InstagramScraper:
    def __init__(self, logger):
        self.logger = logger
        self._n_retry = 3
        self.hashtag = None
    def _get_response(self, **kwargs):
        '''
            dictionary 형태의 response 획득
            :param kwargs: url, headers, params, proxies, ... (same as requests.get)
            :return: response['in_direct', 'headers', 'status_code', 'text']
        '''
        ###requests 도중의 에러 ex) TimeOut, MaxtryError, ProxyError, ClientConnectionError 를 catch 하지 못함
        self._max_get_response_try_num = 3
        _get_response_try_num = 0

        while True:
            try:
                # self.logger.info(f"start//**kwargs:{kwargs}")
                response = requests.get(**kwargs)

            except Exception as e:
                if _get_response_try_num >= self._max_get_response_try_num:
                    self.logger.warning(f"warning - {e} / **kwargs:{kwargs}", extra={"status": e.__class__.__name__})
                    raise RequestException

                if isinstance(type(e), requests.exceptions.ConnectionError) or isinstance(type(e),
                                                                                          requests.exceptions.Timeout):
                    self.logger.debug(f"warning - {e} / **kwargs:{kwargs}", extra={"status": e.__class__.__name__})
                    _get_response_try_num += 1
            else:
                response_data = {'is_redirect': response.is_redirect, 'headers': response.headers,
                                 'status_code': response.status_code, 'text': response.text}
                return response_data


    def _get_text(self, **kwargs):
        # Todo status code 에러처리
        response = self._get_response(**kwargs)
        status_code = response['status_code']

        if status_code == 200:
            self.logger.debug(f"status_code:{status_code}")
            if "not-logged-in" in response.get("text"):
                raise ClientLoginRequiredError
            return response['text']

        elif status_code == 400:
            self.logger.error(f"status_code:{status_code}/BadRequestException")
            raise ClientBadRequestError

        elif status_code == 404:
            self.logger.error(f"status_code:{status_code}/NotFoundException")
            raise HashtagNotFound(f"hashtag not found:{self.hashtag}")

        elif status_code == 429:
            self.logger.error(f"status_code:{status_code}/TooManyRequestsException")
            raise ClientTooManyRequestsError
        else:
            self.logger.fatal(f"status_code:{status_code}/UndefinedStatusException")
            raise ClientUndefinedStatusException

    def _get_text_with_retry(self, **kwargs):
        n_tried = 0
        while True:
            n_tried += 1
            try:
                text = self._get_text(**kwargs)
                self.logger.debug(f"success")
                return text
            except Exception as ex:
                if (n_tried < self._n_retry):
                    self.logger.warning(f"retry wait 5 seconds- {n_tried}/{self._n_retry}:{ex}",
                                        extra={"status": ex.__class__.__name__})
                    time.sleep(5)
                    continue
                else:
                    self.logger.warning(f"retry 횟수 초과", extra={"status": ex.__class__.__name__})
                    raise ex

    def get_raw_instagram_hashtag(self, hashtag_name):
        '''
        scrap_instagram_hashtag_raw 함수를 통해 해시태그 정보 스크래핑
        :param hashtag_name: 해시태그 이름 e.g. "테슬라"
        :return: data-hashtag with post_count, posts, ...
        '''
        self.hashtag = hashtag_name
        headers = {
            'x-ig-app-id': '936619743392459',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36 '
        }
        params = {
            'tag_name': hashtag_name,
        }
        url = f'https://i.instagram.com/api/v1/tags/logged_out_web_info/'
        self.logger.info(f"engine.get_raw_instagram_hashtag // params:{params}, url:{url}")

        raw_hashtag = self._get_text_with_retry(headers=headers, params=params, url=url)

        try:
            response = json.loads(raw_hashtag)
        except:
            self.logger.warning(f"get_raw_instagram_hashtag// hashtag_name:{hashtag_name}")
        else:
            self.logger.info(f"success")
            return response
