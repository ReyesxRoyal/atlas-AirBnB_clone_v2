#!/usr/bin/python3
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

# Define the association table for the Many-To-Many relationship
place_amenity = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

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

    # Relationship with Review
    reviews = relationship("Review", cascade="all, delete-orphan", backref="place")
    
    # DBStorage: Many-To-Many relationship with Amenity
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, backref="places")

    # FileStorage: getter and setter for amenities
    @property
    def amenities(self):
        """Return the list of Amenity instances linked to this Place"""
        return [Amenity.get(amenity_id) for amenity_id in self.amenity_ids]

    @amenities.setter
    def amenities(self, amenity):
        """Add an Amenity.id to the amenity_ids"""
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)

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
            'amenity_ids': self.amenity_ids,  # Include amenity_ids in the dict
        })
        return place_dict

