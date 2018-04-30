#!/usr/bin/python3
from models import db


print(db.find_outgoing(['100735', '10111', '10205674', '1021125', '10649428']))
