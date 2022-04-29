"""Contains the schemas for the KSS demo"""
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class ReturnUser(BaseModel):
    """Model for get responses"""
    name: str
    age: int
    email: EmailStr
    nickname: Optional[str]
    creationDate: datetime = datetime.now()


class CreateUser(BaseModel):
    """Model for POST requests"""
    name: str
    age: int
    email: EmailStr
    nickname: Optional[str]
    extraInfo: Optional[str]
    creationDate: datetime = datetime.now()
