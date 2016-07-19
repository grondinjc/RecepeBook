from pdb import set_trace as dbg
import datetime

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base, as_declarative, declared_attr
from sqlalchemy import Column, Integer, String, BLOB, Boolean, ForeignKey


class Model(object):
    
    @as_declarative()
    class Base(declarative_base()):
        """Base class which provides automated table name
        and surrogate primary key column.
        """
        id = Column(Integer, primary_key=True, autoincrement=True)
        
        @declared_attr
        def __tablename__(cls):
            return cls.__name__.lower()


    ########################################################################
    class Recepe(Base):
        name = Column(String)
        video = Column(BLOB, nullable=True)
        
        tagslist_id = relationship("DescriptiveTag", backref="recepes")


    ########################################################################
    class DescriptiveTag(Base):
        name = Column(String)
     
    
