import cherrypy
from cherrypy import request, HTTPError
from cherrypy.lib import static
from genshi.template import TemplateLoader
from os.path import relpath

from pdb import set_trace as dbg

class HomeController(object):
  """
  Controller of the /Home part
  """

  HTML_TEMPLATE = 'home.html'

  def __init__(self, app, template_path, logger):
    """
    Controller initialiser

    @type app: cide.app.python.core.Core
    @type template_path: str
    @type logger: logging.Logger

    @param app: The core application
    @param template_path: Path to the template directory
    @param logger: The logger instance
    """
    self._app = app
    self._logger = logger

    print template_path
    print template_path
    print template_path
    print template_path
    self._loader = TemplateLoader(search_path=[template_path],
                                  auto_reload=True)

    self._logger.debug("HomeController instance created")

    self._f = open("/home/jc/Desktop/Recepe/RecepeBook/src/web/static/test.mp4")


  @cherrypy.expose
  def index(self):
    """
    Controller index page generator
    (Path : /home/ -- /home/index)

    @return: Template HTML render
    """
    self._logger.info("index requested by ({0}:{1})".format(request.remote.ip,
                                                            request.remote.port))

    tmpl = self._loader.load(self.HTML_TEMPLATE)

    app_name = self._app.get_app_name()
    stream = tmpl.generate(title=app_name)
    return stream.render('html')

  @cherrypy.expose
  def video(self, tag):
    content_type="video/mp4"
    disposition=None #"inline"
    name="test.mp4"
    print tag

    return static.serve_fileobj(self._f, content_type, disposition, name)
