from pydantic import BaseModel


class ImageRequest(BaseModel):
    receipt_description: str
