#!/usr/bin/python3
# models/city.py
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """Representation of city"""
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    places = relationship("Place", cascade="all, delete-orphan", backref="city")

    def __init__(self, *args, **kwargs):
        """Initializes the city instance"""
        super().__init__(*args, **kwargs)
