from json import JSONEncoder, dumps as serialize
from pdb import set_trace as dbg


class CustomEncoder(JSONEncoder):
  def default(self, o):
    return o.__dict__


class Serializer(object):

  @classmethod
  def dumps(cls, reply):
    """
    Convert a reply object to a json string

    @return: json string
    """
    return serialize(reply, cls=CustomEncoder)
