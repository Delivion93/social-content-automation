from typing import TypedDict


class ContentState(TypedDict):
    product: str
    audience: str
    brand_description: str

    campaign_name: str
    concept: str
    tone: str

    instagram_post: str
    facebook_post: str
    linkedin_post: str

    approved: bool
    feedback: list[str]

    revision_count: int