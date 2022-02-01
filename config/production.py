import os
from config.default import *

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_DIR, "pybo.db")}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x8a\xe6\xb6b\x19u\xc73x/M\xdd\xd9\xe5\xe1|'