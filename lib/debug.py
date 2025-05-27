import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import session
from models.book import Book
from models.author import Author
from models.genre import Genre

import ipdb; ipdb.set_trace()
