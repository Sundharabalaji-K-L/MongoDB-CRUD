from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient("mongodb://root:mongo@blog-mongodb:27017/blog")
database = client["auth"]

