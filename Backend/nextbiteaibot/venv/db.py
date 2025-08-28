import motor.motor_asyncio
from bson import ObjectId
import os
from dotenv import load_dotenv


load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL, tlsAllowInvalidCertificates=True)
db = client['nextbite_ai']
recipes_collection = db['recipes']

