from distutils.core import setup
from setuptools import find_packages

from babel.messages import frontend as babel

from fnmatch import fnmatch
import os 

from pdb import set_trace as dbg


PROJECT_NAME = 'RecepeBook'
app_name = PROJECT_NAME.lower()

PROJECT_DESC = 'Local online customizable recepe book'

VERSION_FILE_NAME = 'VERSION' 
REQUIREMENTS_FILE_NAME = 'REQUIREMENTS'
CONF_OUTPUT_DIR = 'prj_config'

META_AUTHOR = "Jean-Christophe Grondin"
META_AUTHOR_EMAIL = "grondin.jc@hotmail.com"
META_URL = 'www.google.com'



def get_version():
    version = "0.0"
    if os.path.isfile(VERSION_FILE_NAME):
        with open(VERSION_FILE_NAME) as f:
            version = f.readline()
    return version


def get_requirements():
    req = []
    if os.path.isfile(REQUIREMENTS_FILE_NAME):
        with open(REQUIREMENTS_FILE_NAME) as f:
            req = [line.rstrip('\n') for line in f]
    return req


def get_packages():
    fmt = app_name + ".{0}"
    subpackages = [fmt.format(p) for p in find_packages('src')]
    return [app_name] + subpackages


def get_files_in_dir(dir_name, pattern):
    fmt = dir_name + '/{0}'
    return [fmt.format(f) for f in os.listdir(dir_name) if fnmatch(f, pattern)]


setup(
    name = PROJECT_NAME,
    version = get_version(),
    description = PROJECT_DESC,
    author = META_AUTHOR,
    author_email = META_AUTHOR_EMAIL,
    url = META_URL,

    # adding requirements
    install_requires = get_requirements(),

    # adding packages
    package_dir = {app_name : 'src'},
    packages = get_packages(),
    
    # add non-python files (must be in MANIFEST)
    package_data = {app_name: ["src/template/*", "src/static/*"]},
    include_package_data = True,

    # export configuration files
    data_files = [(CONF_OUTPUT_DIR, get_files_in_dir('config', "*.conf"))],

    # expose script
    scripts = ['bin/launch_recepebook'],

    # expose translation commands to the setup script
    cmdclass = {'compile_catalog': babel.compile_catalog,
                'extract_messages': babel.extract_messages,
                'init_catalog': babel.init_catalog,
                'update_catalog': babel.update_catalog}
)

