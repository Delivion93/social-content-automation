from pydantic import BaseModel


class CopywriterOutput(BaseModel):
    instagram_post: str
    facebook_post: str
    linkedin_post: str