from pdb import set_trace as dbg
from recepebook.server.db.schema import Schema
from recepebook.server.app.utils.facebookUtils import FacebookUtils

from recepebook.server.messages.reply import ImportBookmarkDetectedGroup


class RecepeBook(object):
  
  def __init__(self, app_name, db_url, logger):
    self._logger = logger
    self._app_name = app_name
    self._db_url = db_url

    # Elements created later
    self._model = None


  def get_app_name(self):
    return self._app_name


  def start(self):
    """
    Start the application
    """
    self._model = Schema.create_session(self._db_url)


  def stop(self):
    """
    Stop the application
    """
    if self._model is not None:
      self._model.stop()


  def get_search_tag(self, prefix=""):
    """
    Returns item tags matching the specified prefix

    @param prefix: prefix of the tag
    @return : array of string
    """
    return [r.name for r in self._model.get_tags(prefix)]


  def get_matching_recepes(self, tags=None):
    """
    Returns item tags matching the specified prefix

    @param tags: the list of tags
    @return : array of Recepe object
    """
    if tags is None:
      tags = []

    f = open("/home/jc/Desktop/Recepe/RecepeBook/src/web/static/test.mp4")
    return f


  def get_detected_recepes_from_bookmarks(self, bookmark_text):
    """
    Returns the detected bookmark from the facebook bookmark page

    @param bookmark_text: The html string of the web page
    @return : list of reply.ImportBookmarkDetectedGroup
    """
    source_links_assoc = FacebookUtils.detect_links_from_html(bookmark_text)
    return [ImportBookmarkDetectedGroup(source, links) 
        for (source, links)
        in source_links_assoc.iteritems()]
