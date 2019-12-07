from pymongo import MongoClient
import settings

class MongoAPI():
    """
        Deals with the connection between
        between our app and the MongoDB.
    """

    def __init__(self):
        """
            Constructor.
        """
        self.client = MongoClient(settings.FULL_CONN)
        self.write = MongoClient(settings.FULL_URL)