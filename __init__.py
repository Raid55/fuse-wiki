'''
    Package initializer
'''

from models.engine import DBStorage
from models.request import Base, Request


# creating db session
storage = DBStorage()
# creating db file and table if not alredy created
storage.reload()
