#!/usr/bin/python3
# models/user.py
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class User(BaseModel, Base):
    """Representation of a user"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    # Relationship with Place
    places = relationship("Place", cascade="all, delete-orphan", backref="user")

    def __init__(self, *args, **kwargs):
        """Initializes user instance"""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Return a dictionary representation of the User instance"""
        user_dict = super().to_dict()  # Call to_dict of BaseModel
        user_dict.update({
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
        })
        return user_dict




