#!/usr/bin/env python
import re
from collections import defaultdict


class FacebookUtils(object):

  GRAPHAPI_URL_FMT = "https://graph.facebook.com/{0}?fields=source"

  TARGET_SITE = 'www.facebook.com'
  URL_GROUP = "recepe_url"
  SOURCE_GROUP = "recepe_source"

  URL_PATTERN = '/(?:[\w\d:#@%/;$~_?\+-=\.&](?:#!)?)+'
  SOURCE_PATTERN = '[\w\d ]+'

  BOOKMARK_REGEX = '(?:<a class="_24-t" href="(?P<{0}>{1})">.+?<span class="blueName">(?P<{2}>{3})<\/span>)+'



  @classmethod
  def convert_url_to_graphapi(cls, url):
    url = url[:-1] if url.endswith("/") else url
    object_id = url[url.rfind("/")+1:]
    return cls.GRAPHAPI_URL_FMT.format(object_id)


  @classmethod
  def detect_links_from_html(cls, html_text):
    links_by_source = defaultdict(list)
    for find_result in cls.BOOKMARK_REGEX.finditer(html_text):
      find_result_dict = find_result.groupdict()
      links_by_source[find_result_dict[cls.SOURCE_GROUP]].append(cls.TARGET_SITE + find_result_dict[cls.URL_GROUP])
    return links_by_source


# Initialize regex
FacebookUtils.BOOKMARK_REGEX = re.compile(FacebookUtils.BOOKMARK_REGEX.format(
  FacebookUtils.URL_GROUP,
  FacebookUtils.URL_PATTERN,
  FacebookUtils.SOURCE_GROUP,
  FacebookUtils.SOURCE_PATTERN)
)
