from future.standard_library import install_aliases
install_aliases()
from urllib.parse import urlparse

def pass_tag(message):
    return '[\033[32mPASS\033[0m]%s' % message


def fail_tag(message):
    return '[\033[31mFAIL\033[0m]%s' % message


def highlight(message):
    return '\033[32m[%s]\033[0m' % message


def is_valid_url(url):
    """Checks if a given string is an url"""
    pieces = urlparse(url)
    return all([pieces.scheme, pieces.netloc])
