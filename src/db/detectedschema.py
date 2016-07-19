"""
The simplest usage is to reflect an existing database into a new model. We create a new AutomapBase class in a similar manner as to how we create a declarative base class, using automap_base(). We then call AutomapBase.prepare() on the resulting base class, asking it to reflect the schema and produce mappings:
"""

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from sqlite3 import dbapi2 as sqlite

from pdb import set_trace as dbg

class Model(object):
	def __init__(self, detected_model):
		self.Recepe = detected_model.classes.Recepe
		self.Tag = detected_model.classes.Tag
		self.RecepeTagAssoc = detected_model.classes.RecepeTagAssoc


def get_connection(dbname):

	# engine, suppose it has two tables 'user' and 'address' set up
	connection_url = "sqlite:///{0}".format(dbname)
	engine = create_engine(connection_url, module=sqlite)

	# reflect the tables
	model_detector = automap_base()
	model_detector.prepare(engine, reflect=True)

	session = Session(engine)
	return session, Model(model_detector)


if __name__ == "__main__":
	conn, model = get_connection("test.db")
	dbg()
	a = 12
