#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Amenity(BaseModel, Base):
    """Representation of an amenity"""
    __tablename__ = 'amenities'
    
    name = Column(String(128), nullable=False)

    # Many-To-Many relationship between Place and Amenity
    place_amenities = relationship("Place", secondary="place_amenity", backref="amenities")

    def __init__(self, *args, **kwargs):
        """Initializes the amenity instance"""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Return a dictionary representation of the Amenity instance"""
        amenity_dict = super().to_dict()  # Call to_dict of BaseModel
        amenity_dict.update({
            'name': self.name,
        })
        return amenity_dict
