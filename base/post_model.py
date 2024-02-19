from pydantic import BaseModel, Field, field_validator
from base.generator import PostGenerator
from enums.global_enums import GlobalErrorMessages


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class CreatePost(BaseModel):
    userId: int = Field(PostGenerator().generate_random_user_id())
    title: str = Field(PostGenerator().generate_random_title())
    body: str = Field(PostGenerator().generate_random_body())

    @field_validator("userId")
    def validate_user_id(cls, userId: int) -> int:
        if userId <= 0:
            raise ValueError(GlobalErrorMessages.WRONG_USER_ID.value)
        return userId
