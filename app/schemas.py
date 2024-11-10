from pydantic import BaseModel, Field
from typing import Optional


class AdCreateSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    owner: str = Field(..., min_length=1, max_length=100)


class AdUpdateSchema(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, min_length=1)


class AdResponseSchema(BaseModel):
    id: int
    title: str
    description: str
    owner: str
    created_at: str
