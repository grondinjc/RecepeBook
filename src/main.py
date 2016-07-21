import sys
import os
import logging
import cherrypy
from configobj import ConfigObj

from recepebook.server.homeController import HomeController
from recepebook.app.recepebook import RecepeBook
from pdb import set_trace as dbg 

def abort_launch(msg):
  cherrypy.log(msg)
  sys.exit(1)


# Read config file name from command parameters
if len(sys.argv) != 2:
  error_msg = "Missing or too many arguments. "
  error_msg += "Usage : python {0} <configs_file>".format(sys.argv[0])
  abort_launch(error_msg)
else:
  configs_file = sys.argv[1]

# Get the server and app config from the config file received
bin_dir = os.path.abspath(os.path.dirname(__file__))
templates_dir = os.path.normpath(os.path.join(bin_dir, '../src/templates'))
compiled_dir = os.path.normpath(os.path.join(bin_dir, '../src/static/css'))

# Configuration objects to fetch information from
configs = ConfigObj(configs_file)

# General configurations
prj_name = configs['DEFAULT']['project_name']
prj_log_file = configs['LOGGERS']['log_file']
prj_template_dir = configs['APP']['templates']

# Server and controller configurations
conf_file_server = configs['APP']['server']
conf_file_controllerHome = configs['APP']['homeController']

# Setup Log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s')
handler = logging.FileHandler(prj_log_file)
handler.setFormatter(formatter)
logger = logging.getLogger('recepebook')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

# Set server config with config file
cherrypy.config.update(conf_file_server)

# Instanciate App
app = RecepeBook(prj_name, logger)

# Bind for server event (start/stop)
cherrypy.engine.subscribe('start', app.start)
cherrypy.engine.subscribe('stop', app.stop)

# Map URI path to controllers
cherrypy.tree.mount(HomeController(app, prj_template_dir, logger), 
                    "/", conf_file_controllerHome)

# Start server
cherrypy.engine.start()
cherrypy.engine.block()
