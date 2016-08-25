import codecs
from math import sqrt

users = {
    "Tony": {"python": 3.5, "go": 4, "js": 3},
    "Kenneth": {"python": 5, "go": 3, "js": 4},
    "Leo": {"python": 4, "go": 1, "js": 5}
}


class Recommender(object):

    def __init__(self, data, k=1, metric='language', n=5):
        self.k = k
        self.n = n
        self.username =
