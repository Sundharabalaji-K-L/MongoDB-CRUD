from database import database
from models import PostModel
from schemas import PostCreate
from bson import ObjectId


async def addPost(post: PostCreate):
    result = await database["posts"].insert_one(post.model_dump())

    return PostModel(**post.model_dump(), _id=result.inserted_id).serialize_model()

async def getPost(post_id: str):
    post = await database["posts"].find_one({"_id": ObjectId(post_id)})
    
    if post:
        return PostModel(**post).serialize_model()
    return None


async def getPosts(skip: int = 0, limit:int = 10):
    posts = await database['posts'].find().skip(skip).limit(limit).to_list(limit)
    if posts:
        posts=[PostModel(**post).serialize_model() for post in posts]

        return posts
    
    return None


async def ModifyPost(post_id: str, post: PostCreate):
 updated_result = await database["posts"].update_one(
     {'_id':ObjectId(post_id)},
     {'$set': post.model_dump()}
 )

 if updated_result.modified_count == 0:
     return None
 
 updated_post = post = await database["posts"].find_one({"_id": ObjectId(post_id)})
  
 return PostModel(**updated_post).serialize_model()


async def deletePost(post_id: str):
    deleted_result = await database['posts'].delete_one({'_id': ObjectId(post_id)})
    
    if deleted_result.deleted_count == 0:
        return None
    
    return deleted_result.deleted_count
