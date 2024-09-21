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
    if post:
        return PostResponse.model_validate(post)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found")


@app.get("/posts", response_model=list[PostResponse])
async def get_posts(skip:int = 0, limit:int = 10):
    posts = await getPosts(skip, limit)
    if posts:
        return [PostResponse.model_validate(post) for post in posts]

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found")

@app.put("/update/{post_id}", response_model=PostResponse)
async def update_post(post: PostCreate, post_id: str):
    updated_post = await ModifyPost(post_id, post)
    if updated_post:
        return PostResponse.model_validate(updated_post)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found")

@app.delete("/delete/{post_id}")
async def delete_post(post_id: str):
    result = await deletePost(post_id)

    if result:
        return {"message": "post deleted successfully"}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post Not Found")




