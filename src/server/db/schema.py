"""
The simplest usage is to reflect an existing database into a new model. We create a new AutomapBase class in a similar manner as to how we create a declarative base class, using automap_base(). We then call AutomapBase.prepare() on the resulting base class, asking it to reflect the schema and produce mappings:
"""
from sqlite3 import dbapi2 as sqlite

from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

from sqlalchemy.orm import Session
from sqlalchemy.orm import aliased

from pdb import set_trace as dbg



class Schema(object):

    @classmethod
    def create_session(cls, database_url):
        engine = create_engine(database_url, module=sqlite)

        # reflect the tables
        model_detector = automap_base()
        model_detector.prepare(engine, reflect=True)

        return _Model(model_detector, Session(engine))


    @classmethod
    def create_schema(cls, force=False):
        pass


class _Model(object):

    _TABLES = ['Recepe', 'Tag', 'RecepeTagAssoc']

    def __init__(self, model, session):
        self._session = session

        # Detect and get references to desired tables
        inserter = lambda table: setattr(self, table, getattr(model.classes, table))
        if all(hasattr(model.classes, table) for table in self._TABLES):
            map(inserter, self._TABLES)
        else:
            raise Exception("Database does not have expected table {0}".format(self._TABLES))



    def stop(self):
        """
        Stop the model
        """
        if self._session is not None:
            self._session.close_all()



    def get_tags(self, prefix=""):
        return self._session.query(self.Tag, self.Tag.name).all()

