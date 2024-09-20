from pydantic import BaseModel, Field


class PostBase(BaseModel):
    title: str
    description: str


class PostCreate(PostBase):
    pass


class PostResponse(BaseModel):
    id: str
    title: str
    description: str

    class Config:
         from_attriburtes = True


