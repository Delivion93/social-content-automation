from pydantic import BaseModel


class CampaignEdition(BaseModel):
    campaign_name: str
    concept: str
    tone: str
    instagram_post: str
    facebook_post: str
    linkedin_post: str