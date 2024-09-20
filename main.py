from fastapi import HTTPException, status, FastAPI
from crud import addPost, getPost, getPosts, ModifyPost, deletePost
from schemas import PostResponse, PostCreate

app = FastAPI()

@app.post("/", response_model=PostResponse)
async def create_post(post: PostCreate):
    new_post = await addPost(post)

    return PostResponse.model_validate(new_post)


@app.get("/post/{post_id}", response_model=PostResponse)
async def get_post(post_id: str):
    post = await getPost(post_id)

    return PostResponse.model_validate(post)


@app.get("/posts", response_model=list[PostResponse])
async def get_posts(skip:int = 0, limit:int = 10):
    posts = await getPosts(skip, limit)

    return [PostResponse.model_validate(post) for post in posts]


@app.put("/update/{post_id}", response_model=PostResponse)
async def update_post(post: PostCreate, post_id: str):
    updated_post = await ModifyPost(post_id, post)

    return PostResponse.model_validate(updated_post)


@app.delete("/delete/{item_id}")
async def delete_post(post_id: str):
    if deletePost(post_id):
        return {'message': 'post deleted successfully'}
    
    return None

