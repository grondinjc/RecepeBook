import cherrypy
from cherrypy import request, HTTPError
from cherrypy.lib import static
from os.path import relpath

import locale
from pdb import set_trace as dbg

class HomeController(object):
  """
  Controller of the /Home part
  """

  HTML_TEMPLATE = 'home.html'

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

    self._logger.debug("HomeController instance created")


  @cherrypy.expose
  def index(self):
    """
    Controller index page generator
    (Path : / or /index)

    @return: HTML template to render
    """
    self._logger.info("index requested by ({0}:{1})".format(request.remote.ip,
                                                            request.remote.port))

    locale.setlocale(locale.LC_ALL, 'en_US')
    tmpl = self._loader.get_template(self.HTML_TEMPLATE)
    return tmpl.render(title=self._app.get_app_name())


  @cherrypy.expose
  def video(self, tag, **params):
    """
    Controller for ajax request
    (Path : /video)

    @return: 
    """
    content_type = "video/mp4"
    disposition = "inline"
    name = "test.mp4"

    f = self._app.get_matching_recepes(tag)
    return static.serve_fileobj(f, content_type, disposition, name)

  @cherrypy.expose
  def test(self):
    tags = self._app.get_search_tag("")
    return ",".join(tags)