
from pydantic import BaseModel
from typing import List



from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List

class Event(SQLModel, table= True):
    id: int = Field(default= None, primary_key= True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column= Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://bilmemne.jpeg",
                "description": "Content",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }


class EventUpdate(SQLModel):
    title: Optional[str]
    image: Optional[str]
    description: Optional[str]
    tags: Optional[List[str]]
    location: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://bilmemne.jpeg",
                "description": "Content",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }