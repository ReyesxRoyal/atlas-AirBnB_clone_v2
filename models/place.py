#!/usr/bin/python3
# models/place.py
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from models.base_model import BaseModel, Base

class Place(BaseModel, Base):
    """Representation of a place"""
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    def __init__(self, *args, **kwargs):
        """Initializes the place instance"""
        super().__init__(*args, **kwargs)

    def to_dict(self):
        """Return a dictionary representation of the Place instance"""
        place_dict = super().to_dict()  # Call to_dict of BaseModel
        place_dict.update({
            'city_id': self.city_id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'number_rooms': self.number_rooms,
            'number_bathrooms': self.number_bathrooms,
            'max_guest': self.max_guest,
            'price_by_night': self.price_by_night,
            'latitude': self.latitude,
            'longitude': self.longitude,
        })
        return place_dict

