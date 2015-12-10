# encoding: utf-8
# module hiredis.hiredis
# from /usr/local/lib/python2.7/site-packages/hiredis/hiredis.so
# by generator 1.137
# no doc

# imports
import hiredis as __hiredis


# no functions
# classes

class HiredisError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ProtocolError(__hiredis.HiredisError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Reader(object):
    """ Hiredis protocol reader """
    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def getmaxbuf(self, *args, **kwargs): # real signature unknown
        pass

    def gets(self, *args, **kwargs): # real signature unknown
        pass

    def setmaxbuf(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass


class ReplyError(__hiredis.HiredisError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


