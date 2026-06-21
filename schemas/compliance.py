from pydantic import BaseModel


class ComplianceReport(BaseModel):
    approved: bool
    feedback: list[str]