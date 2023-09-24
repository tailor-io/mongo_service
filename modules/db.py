from flask_pymongo import pymongo
import os
import certifi

CONNECTION_STRING = os.getenv("MONGO_URI")


class DB:
    def __init__(self) -> None:
        ca = certifi.where()
        client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=ca)
        # self.database = client.get_database("flask_mongodb_atlas")
        self.database = client.get_database("tailor_app")

    def getUserInfo(self, user_id: str):
        """_summary_

        Args:
            user_id (str): _description_
        """
        user_collection = pymongo.collection.Collection(self.database, "personal_info")
        query_result = user_collection.find_one({"user_id": user_id})
        return query_result

    def createUserInfo(self, user_info):
        """_summary_

        Args:
            user_id (str): _description_
        """
        user_collection = pymongo.collection.Collection(self.database, "personal_info")
        query_result = user_collection.insert_one(user_info)
        return query_result

    def getUserExperience(self, user_id: str):
        """_summary_

        Args:
            user_id (str): _description_
        """
        user_collection = pymongo.collection.Collection(
            self.database, "experience_info"
        )

        query_result = []
        for experience in user_collection.find({"user_id": user_id}):
            del experience["_id"]
            query_result.append(experience)

        return query_result

    def createUserExperience(self, experience):
        """_summary_

        Args:
            user_id (str): _description_
        """
        user_collection = pymongo.collection.Collection(
            self.database, "experience_info"
        )
        query_result = user_collection.insert_one(experience)
        return query_result

    def getUserEducation(self, user_id: str):
        """_summary_

        Args:
            user_id (str): _description_
        """
        user_collection = pymongo.collection.Collection(self.database, "education")

        query_result = []
        for education in user_collection.find({"user_id": user_id}):
            del education["_id"]
            query_result.append(education)

        return query_result

    def createUserEducation(self, education):
        """_summary_

        Args:
            user_id (str): _description_
        """
        user_collection = pymongo.collection.Collection(self.database, "education")
        query_result = user_collection.insert_one(education)
        return query_result
