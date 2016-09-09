import cherrypy
from cherrypy import request, HTTPError
from cherrypy.lib import static
from os.path import relpath

from recepebook.server.controller.utils.serializer import Serializer
from pdb import set_trace as dbg
dumps = Serializer.dumps


class ImportController(object):
  """
  Controller of the /Import part
  """

  HTML_TEMPLATE = 'import.html'

  def __init__(self, app, loader, logger):
    """
    Controller initialiser

    @type app: cide.app.python.core.Core
    @type loader: jinja2.Environment
    @type logger: logging.Logger

    @param app: The core application
    @param template_path: Path to the template directory
    @param logger: The logger instance
    """
    self._app = app
    self._logger = logger
    self._loader = loader

    self._logger.debug("ImportController instance created")


  @cherrypy.expose
  def index(self):
    """
    Controller index page generator
    (Path : / or /index)

    @return: HTML template to render
    """
    self._logger.info("index requested by ({0}:{1})".format(request.remote.ip,
                                                            request.remote.port))

    tmpl = self._loader.get_template(self.HTML_TEMPLATE)
    return tmpl.render(title=self._app.get_app_name())

  @cherrypy.expose
  @cherrypy.tools.allow(methods=['POST'])
  def detect_bookmark_links(self, bookmark_text, **kwargs):
    """
    Controller request handler page generator
    (Path : /bookmark)

    @return: HTML template to render
    """
    return dumps(self._app.get_detected_recepes_from_bookmarks(bookmark_text))
    