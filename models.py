from pydantic import BaseModel, Field, model_serializer
from bson import ObjectId


class PostModel(BaseModel):
    id: ObjectId = Field(alias="_id")
    title: str
    description: str

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

    @model_serializer
    def serialize_model(self):
        serialized = self.__dict__.copy()
        serialized['id'] = str(serialized['id'])
        return serialized

