from pydantic import BaseModel
from typing import Optional

# This validates the data coming IN from the user when creating a note
class NoteCreate(BaseModel):
    title: Optional[str] = None
    content: str

# This shapes the data going OUT from the API back to the user
class NoteResponse(BaseModel):
    id: int
    title: Optional[str] = None
    content: str

    class Config:
        from_attributes = True