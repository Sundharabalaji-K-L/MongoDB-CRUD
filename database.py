from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient("mongodb://root:mongo@mongodb:27017/")
database = client["blog"]

