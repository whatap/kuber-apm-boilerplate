from requests import RequestException


# class InstagramScraperError(Exception):
#     """Base Exception for instagram_scraper"""

class ScraperError(Exception):
    """Base Exception for engines.raw_scraper"""
    pass

class ScraperSchemaError(ScraperError):
    """Base Exception for engines.raw_scraper"""
    pass

class ExtractorSchemaError(ScraperError):
    """Base Exception for engines.raw_scraper"""
    pass
class ClientRequestError(ScraperError):
    pass


class ClientBadRequestError(ClientRequestError):
    """Raised due to a HTTP 400 response"""

class ClientLoginRequiredError(ClientRequestError):
    """Raised due to a LOGIN REQUIRED"""

class ClientForbiddenError(ClientRequestError):
    """Raised due to a HTTP 403 response"""


class ClientNotFoundError(ClientRequestError):
    """Raised due to a HTTP 404 response"""


class ClientTooManyRequestsError(ClientRequestError):
    """Raised due to a HTTP 429 response"""


class ClientWrongRequestError(ClientRequestError):
    """there was a problem with your request"""


class ClientUndefinedStatusException(ClientRequestError):
    """undefined HTTP error code"""


class UserError(ScraperError):
    """Raised due to instagram user scraper"""
    pass


class UserNotFound(UserError):
    """when user not exist"""
    pass


class HashtagError(ScraperError):
    """Raised due to instagram hashtag scraper"""
    pass


class HashtagNotFound(HashtagError):
    """when hashtag not exist"""
    pass


class LocationError(ScraperError):
    """Raised due to instagram location scraper"""
    pass


class LocationNotFound(HashtagError):
    """when location not exist"""
    pass


class MediaError(ScraperError):
    """Raised due to instagram media scraper"""
    pass


class MediaNotFound(MediaError):
    """when media not exist"""
    pass


class ParsingError(ScraperError):
    """Raised due to instagram raw data parsing"""
    pass


class RawDataParsingError(ParsingError):
    """Key Error while Parsing"""

class LamadavaServerError(ScraperError):
    """Raised due to lamadava server"""
    pass