from pymongo import MongoClient
import settings
import json
from bson import json_util

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
        self.acessos = self.client.smartroom.credential

    def getAllCards(self):
        lista = []
        for i in self.acessos.find({}, {'_id': False, '_class': False}):
            lista.append(json.loads(json_util.dumps(i)))
        return lista

    def getCards(self, home):
        lista = []
        for i in self.acessos.find({'home':int(home)}, {'_id': False, '_class':False}):
            lista.append(json.loads(json_util.dumps(i)))
        return lista